from ultralytics import YOLO
import openvino, sys, shutil, os

# -------------------------------
# Configuration
# -------------------------------
model_name = 'yolo11s'
model_type = 'yolo_v11'

# model_name = 'yolov8s'
# model_type = 'yolo_v8'


weights = model_name + '.pt'
model_dir = f"dlstreamer_omz/models/{model_name}"

# Create FP32 and FP16 folders
fp32_dir = os.path.join(model_dir, "FP32")
fp16_dir = os.path.join(model_dir, "FP16")
os.makedirs(fp32_dir, exist_ok=True)
os.makedirs(fp16_dir, exist_ok=True)

# -------------------------------
# Load YOLO model
# -------------------------------
model = YOLO(weights)
model.info()

# -------------------------------
# Export to OpenVINO IR format
# -------------------------------
converted_path = model.export(format='openvino')
converted_model = os.path.join(converted_path, model_name + '.xml')

# -------------------------------
# Read and modify OpenVINO model
# -------------------------------
core = openvino.Core()
ov_model = core.read_model(model=converted_model)

if model_type in ["YOLOv8-SEG", "yolo_v11_seg"]:
    ov_model.output(0).set_names({"boxes"})
    ov_model.output(1).set_names({"masks"})

ov_model.set_rt_info(model_type, ['model_info', 'model_type'])

# -------------------------------
# Save FP32 and FP16 models in their respective folders
# -------------------------------
fp32_path = os.path.join(fp32_dir, model_name + '.xml')
fp16_path = os.path.join(fp16_dir, model_name + '.xml')

openvino.save_model(ov_model, fp32_path, compress_to_fp16=False)
openvino.save_model(ov_model, fp16_path, compress_to_fp16=True)

# -------------------------------
# Cleanup
# -------------------------------
shutil.rmtree(converted_path)
os.remove(weights)

print(f"FP32 model saved in: {fp32_dir}")
print(f"FP16 model saved in: {fp16_dir}")
