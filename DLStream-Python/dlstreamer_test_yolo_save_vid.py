# ==============================================================================
# Copyright (C) 2025 Intel Corporation
#
# SPDX-License-Identifier: MIT
# ==============================================================================

import sys
import os
import gi
import datetime

gi.require_version("GstVideo", "1.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gst", "1.0")
gi.require_version("GstAnalytics", "1.0")
from gi.repository import GLib, Gst, GstAnalytics
from gstgva import VideoFrame

# -------------------------
# Probe (unchanged, minor tidy)
# -------------------------
def watermark_sink_pad_buffer_probe(pad, info, u_data):
    buffer = info.get_buffer()
    if buffer is None:
        return Gst.PadProbeReturn.OK

    # -------------------------------
    # Extract GVA detection metadata
    # -------------------------------
    frame = VideoFrame(buffer)

    for roi in frame.regions():
        # Safely get fields (method or attribute)
        def safe_get(obj, name, default=None):
            val = getattr(obj, name, default)
            return val() if callable(val) else val

        label = safe_get(roi, "label", "unknown")
        conf  = safe_get(roi, "confidence", 0.0)
        rect  = safe_get(roi, "rect", None)

        if rect:
            print(f"[GVA] {label} | {conf:.2f} | "
                  f"({rect.x:.1f}, {rect.y:.1f}, {rect.w:.1f}, {rect.h:.1f})")
        else:
            print(f"[GVA] {label} | {conf:.2f} | <no box>")

    # -------------------------------
    # Extract Analytics metadata
    # -------------------------------
    rmeta = GstAnalytics.buffer_get_analytics_relation_meta(buffer)

    if rmeta:
        obj_counter = {}
        for mtd in rmeta:
            if isinstance(mtd, GstAnalytics.ODMtd):
                cls = GLib.quark_to_string(mtd.get_obj_type())
                obj_counter[cls] = obj_counter.get(cls, 0) + 1

        print(f"[Analytics] {obj_counter}")

        # attach a simple text metadata (example)
        rmeta.add_one_cls_mtd(
            1.0,
            GLib.quark_from_string(str(obj_counter))
        )

    return Gst.PadProbeReturn.OK


# -------------------------
# Helper: link decodebin -> next element (video pad only)
# -------------------------
def on_decodebin_pad_added(decodebin, pad, target):
    if pad is None:
        return
    caps = pad.get_current_caps()
    if not caps:
        caps = pad.query_caps()
    caps_str = caps.to_string()
    # only link video pads
    if not caps_str.startswith("video/"):
        return

    sink_pad = target.get_static_pad("sink")
    if not sink_pad:
        # element might expose request pads instead - try request pad
        try:
            sink_pad = target.get_request_pad("sink_0")
        except Exception:
            sink_pad = None

    if sink_pad and not sink_pad.is_linked():
        pad.link(sink_pad)


# -------------------------
# Main
# -------------------------
def main(args):
    Gst.init(None)

    if len(args) != 3:
        sys.stderr.write("usage: %s <LOCAL_VIDEO_FILE> <LOCAL_MODEL_FILE>\n" % args[0])
        sys.exit(1)

    video_path = args[1]
    model_path = args[2]

    # create outdir and filename
    os.makedirs("./outdir", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(os.path.abspath("./outputs"), f"dlstream_output_{timestamp}.mp4")
    print(f"Saving MP4 output to: {output_file}")

    # -------------------------
    # Create pipeline and elements
    # -------------------------
    pipeline = Gst.Pipeline.new("dlstream-pipeline")
    if not pipeline:
        sys.stderr.write(" Unable to create Pipeline \n")
        sys.exit(1)

    # Source & decode
    source = Gst.ElementFactory.make("filesrc", "file-source")
    source.set_property("location", video_path)
    decoder = Gst.ElementFactory.make("decodebin3", "decoder")

    # GVA inference
    detect = Gst.ElementFactory.make("gvadetect", "gvadetect")
    detect.set_property("model", model_path)
    # device can be "CPU" or "GPU" depending on your setup
    detect.set_property("device", "GPU")
    detect.set_property("batch-size", 1)

    # watermark / overlay
    watermark = Gst.ElementFactory.make("gvawatermark", "watermark")

    videoconvert = Gst.ElementFactory.make("videoconvert", "videoconvert")

    # tee to branch preview + save
    tee = Gst.ElementFactory.make("tee", "tee")

    # preview branch
    q_preview = Gst.ElementFactory.make("queue", "queue-preview")
    videosink = Gst.ElementFactory.make("autovideosink", "video-sink")
    videosink.set_property("sync", False)

    # save branch
    q_save = Gst.ElementFactory.make("queue", "queue-save")
    x264 = Gst.ElementFactory.make("x264enc", "x264-encoder")
    # tune x264 encoder for low-latency recordings; adjust as needed
    try:
        x264.set_property("bitrate", 5000)  # kbps
        x264.set_property("speed-preset", "ultrafast")
        x264.set_property("tune", "zerolatency")
    except Exception:
        # some x264enc builds use different property names - ignore if not available
        pass
    mp4mux = Gst.ElementFactory.make("mp4mux", "mp4-mux")
    filesink = Gst.ElementFactory.make("filesink", "file-sink")
    filesink.set_property("location", output_file)
    filesink.set_property("sync", False)

    # intermediate queue between detect and watermark to decouple inference
    q_before_wm = Gst.ElementFactory.make("queue", "queue-before-watermark")

    # sanity checks
    elements = [
        source, decoder, detect, q_before_wm, watermark, videoconvert, tee,
        q_preview, videosink, q_save, x264, mp4mux, filesink
    ]
    for e in elements:
        if e is None:
            sys.stderr.write("Failed to create one or more GStreamer elements. Check your GStreamer/DLStreamer installation.\n")
            sys.exit(1)

    # add elements to pipeline
    for e in elements:
        pipeline.add(e)

    # link static portions
    # filesrc -> decodebin3 (dynamic link via pad-added)
    # decodebin3 -> gvadetect (via pad-added callback)
    # gvadetect -> queue_before_wm -> watermark -> videoconvert -> tee
    if not detect.link(q_before_wm):
        print("Failed to link detect -> q_before_wm")
    if not q_before_wm.link(watermark):
        print("Failed to link q_before_wm -> watermark")
    if not watermark.link(videoconvert):
        print("Failed to link watermark -> videoconvert")
    if not videoconvert.link(tee):
        print("Failed to link videoconvert -> tee")

    # branch 1 (preview): tee -> q_preview -> videosink
    # request a tee src pad
    tee_preview_pad = tee.get_request_pad("src_%u")
    if tee_preview_pad is None:
        print("Failed to get request pad for tee (preview)")
        sys.exit(1)
    if not tee.link(q_preview):
        # if direct link fails, link explicitly using pads
        q_preview_sink = q_preview.get_static_pad("sink")
        tee_preview_pad.link(q_preview_sink)
    if not q_preview.link(videosink):
        print("Failed to link preview queue -> videosink")

    # branch 2 (save): tee -> q_save -> x264 -> mp4mux -> filesink
    tee_save_pad = tee.get_request_pad("src_%u")
    if tee_save_pad is None:
        print("Failed to get request pad for tee (save)")
        sys.exit(1)
    # link tee -> q_save
    q_save_sink = q_save.get_static_pad("sink")
    tee_save_pad.link(q_save_sink)
    if not q_save.link(x264):
        print("Failed to link q_save -> x264")
    if not x264.link(mp4mux):
        print("Failed to link x264 -> mp4mux")
    if not mp4mux.link(filesink):
        print("Failed to link mp4mux -> filesink")

    # connect decodebin pad-added to gvadetect
    decoder.connect("pad-added", on_decodebin_pad_added, detect)

    # link filesrc -> decodebin
    if not source.link(decoder):
        print("Failed to link source -> decoder")

    # attach probe to watermark sink pad
    wm_sinkpad = watermark.get_static_pad("sink")
    if not wm_sinkpad:
        sys.stderr.write(" Unable to get sink pad of gvawatermark \n")
    else:
        wm_sinkpad.add_probe(Gst.PadProbeType.BUFFER, watermark_sink_pad_buffer_probe, 0)

    # -------------------------
    # Run
    # -------------------------
    print("Starting Pipeline")
    bus = pipeline.get_bus()
    pipeline.set_state(Gst.State.PLAYING)

    terminate = False
    while not terminate:
        msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS | Gst.MessageType.ERROR)
        if msg:
            if msg.type == Gst.MessageType.ERROR:
                err, debug_info = msg.parse_error()
                src_name = msg.src.get_name() if msg.src else "unknown"
                print(f"Error received from element {src_name}")
                print(f"Debug info: {debug_info}")
                terminate = True
            elif msg.type == Gst.MessageType.EOS:
                print("Pipeline complete.")
                terminate = True

    pipeline.set_state(Gst.State.NULL)
    print("Pipeline stopped cleanly")


if __name__ == '__main__':
    sys.exit(main(sys.argv))
