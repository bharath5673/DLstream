# ==============================================================================
# Copyright (C) 2025 Intel Corporation
#
# SPDX-License-Identifier: MIT
# ==============================================================================

import sys
import gi
gi.require_version("GstVideo", "1.0")
gi.require_version("GLib", "2.0")
gi.require_version("Gst", "1.0")
gi.require_version("GstAnalytics", "1.0")
from gi.repository import GLib, Gst, GstAnalytics
from gstgva import VideoFrame
import datetime



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

        rmeta.add_one_cls_mtd(
            1.0,
            GLib.quark_from_string(str(obj_counter))
        )

    return Gst.PadProbeReturn.OK






def main(args):
    # STEP 0 - Initialize GStreamer and check input arguments.
    Gst.init(None)
    if len(args) != 3:
        sys.stderr.write("usage: %s <LOCAL_VIDEO_FILE> <LOCAL_MODEL_FILE>\n" % args[0])
        sys.exit(1)


    # STEP 1 - Create GStreamer Pipeline.
    print("Creating Pipeline.\n")
    pipeline = watermark = None
    method = "SIMPLE"
    if method == "SIMPLE":
       # SIMPLE method - from gst-launch equivalent
        pipeline = Gst.parse_launch(
            f"filesrc location={args[1]} ! decodebin3 ! "
            f"gvadetect model={args[2]} device=GPU batch-size=1 ! queue ! "
            f"gvawatermark name=watermark ! videoconvertscale ! autovideosink"
        )
        watermark = pipeline.get_by_name("watermark")
    else:
        # FULL method instantiating and linking individual elements
        pipeline = Gst.Pipeline()
        if not pipeline:
            sys.stderr.write(" Unable to create Pipeline \n")

        print("Creating Pipeline Elements  \n ")
        # Source element for reading from the file
        source = Gst.ElementFactory.make("filesrc", "file-source")
        if not source:
            sys.stderr.write(" Unable to create Source \n")

        # Use vah264 hardware accelerated decode on GPU
        decoder = Gst.ElementFactory.make("decodebin3", "media-decoder")
        if not decoder:
            sys.stderr.write(" Unable to create Media Decoder \n")

        # gvadetect to detect objects in video frames
        detect = Gst.ElementFactory.make("gvadetect", "object detector")
        if not detect:
            sys.stderr.write(" Unable to create gvadetect element \n")

        # Queue element decopules AI inference from rest of the pipeline
        queue = Gst.ElementFactory.make("queue", "queue")
        if not queue:
            sys.stderr.write(" Unable to create queue element \n")

        # Create gvawatermark to overlay prediction results on video frames
        watermark = Gst.ElementFactory.make("gvawatermark", "watermark")
        if not watermark:
            sys.stderr.write(" Unable to create gvawatermark element \n")

        videoconvertscale = Gst.ElementFactory.make("videoconvertscale", "videoconvertscale")
        if not videoconvertscale:
            sys.stderr.write(" Unable to create videoconvertscale element \n")

        # Create audio-video sink element to display decoding results
        sink = Gst.ElementFactory.make("autovideosink", "sink")
        if not sink:
            sys.stderr.write(" Unable to create sink element \n")



        # # Create output directory and better file naming
        # os.makedirs("./outputs", exist_ok=True)
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # sink.set_property("location", f"/root/outputs/dlstream_test_yolo_save_vid_out_{timestamp}.mp4")


        # Configure elements
        print("Playing file %s " %args[1])
        source.set_property('location', args[1])
        detect.set_property('batch-size', 1)
        detect.set_property('device', "GPU")
        detect.set_property('model', args[2])

        print("Adding elements to Pipeline \n")
        pipeline.add(source)
        pipeline.add(decoder)
        pipeline.add(detect)
        pipeline.add(queue)
        pipeline.add(watermark)
        pipeline.add(videoconvertscale)
        pipeline.add(sink)

        # Link elements, late binding for decode->detect
        print("Linking elements in the Pipeline \n")
        source.link(decoder)
        decoder.connect("pad-added",
                        lambda element, pad, data: element.link(data) if pad.get_name().find("video") != -1 and not pad.is_linked() else None, 
                        detect)
        detect.link(queue)
        queue.link(watermark)
        watermark.link(videoconvertscale)
        videoconvertscale.link(sink)

    # STEP 2 - Add custom probe to the sink pad of the gvawatermark element.
    watermarksinkpad = watermark.get_static_pad("sink")
    if not watermarksinkpad:
        sys.stderr.write(" Unable to get sink pad of gvawatermark \n")
    watermarksinkpad.add_probe(Gst.PadProbeType.BUFFER, watermark_sink_pad_buffer_probe, 0)    

    # STEP 3 - Eexecute pipeline.
    print("Starting Pipeline \n")
    bus = pipeline.get_bus()
    pipeline.set_state(Gst.State.PLAYING)
    terminate = False
    while not terminate:
        msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE, Gst.MessageType.EOS | Gst.MessageType.ERROR)
        if msg:
            if msg.type == Gst.MessageType.ERROR:
                _, debug_info = msg.parse_error()
                print(f"Error received from element {msg.src.get_name()}")
                print(f"Debug info: {debug_info}")
                terminate = True                
            if msg.type == Gst.MessageType.EOS:
                print(f"Pipeline complete.")
                terminate = True
    pipeline.set_state(Gst.State.NULL)

if __name__ == '__main__':
    sys.exit(main(sys.argv))













# In DLStreamer, the method for extracting metadata from the GStreamer buffer is very similar to DeepStream’s OSD probe, but the APIs and metadata structures are different.

# DeepStream uses:
# NvDsBatchMeta → NvDsFrameMeta → NvDsObjectMeta

# DLStreamer uses:
# GstBuffer → GVAMeta → ROI/Detection metadata

# So let me show you exactly how to extract detection metadata in DLStreamer, the same way you do in DeepStream’s osd_sink_pad_buffer_probe.