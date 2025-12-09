# from ultralytics import YOLO
# from openvino.runtime import Core
# import os

# # --------------------------
# # 1. SET MODEL NAME & PATHS
# # --------------------------
# model_dir = "dlstreamer_omz/models"
# os.makedirs(model_dir, exist_ok=True)

# model_name = "yolo11n"        # (or yolov8n, yolov8s, etc.)
# model_pt_path = f"{model_dir}/{model_name}.pt"


# # --------------------------
# # 2. DOWNLOAD MODEL (if not present)
# # --------------------------
# if not os.path.exists(model_pt_path):
#     print("Downloading model...")
#     model = YOLO(model_name)
#     model.save(model_pt_path)
# else:
#     print("Model already exists.")


# # --------------------------
# # 3. EXPORT TO OPENVINO IR
# # --------------------------
# print("Exporting to OpenVINO...")

# model = YOLO(model_pt_path)
# exported_path = model.export(format="openvino")

# print("Export complete:", exported_path)


# # --------------------------
# # 2. REMOVE .pt in CURRENT PATH
# # --------------------------
# pt_file = f"./{model_name}.pt"
# if os.path.exists(pt_file):
#     os.remove(pt_file)
#     print(f"Removed: {pt_file}")
# else:
#     print("No .pt file found in current path.")

# # --------------------------
# # 4. LOAD OPENVINO MODEL
# # --------------------------
# # OpenVINO export creates a folder:
# # dlstreamer/models/yolo11n_openvino_model/
# openvino_model_folder = f"{model_dir}/{model_name}_openvino_model"

# xml_path = f"{openvino_model_folder}/{model_name}.xml"

# print("Loading OpenVINO model:", xml_path)

# ie = Core()
# model_ov = ie.read_model(model=xml_path)

# for i, out in enumerate(model_ov.outputs):
#     try:
#         print(i, " → name:", out.get_tensor().get_names(), "shape:", out.shape)
#     except:
#         print(i, " → name:", "{NO_NAME}", "shape:", out.shape)

# compiled_model = ie.compile_model(model_ov, device_name="CPU")

# print("OpenVINO model loaded successfully!")



# from ultralytics import YOLO
# import openvino, sys, shutil, os

# model_name = 'yolo11s'
# model_type = 'yolo_v11'
# weights = model_name + '.pt'
# model = YOLO(weights)
# model.info()

# converted_path = model.export(format='openvino')
# converted_model = converted_path + '/' + model_name + '.xml'

# core = openvino.Core()

# ov_model = core.read_model(model=converted_model)
# if model_type in ["YOLOv8-SEG", "yolo_v11_seg"]:
#     ov_model.output(0).set_names({"boxes"})
#     ov_model.output(1).set_names({"masks"})
# ov_model.set_rt_info(model_type, ['model_info', 'model_type'])

# openvino.save_model(ov_model, './FP32/' + model_name + '.xml', compress_to_fp16=False)
# openvino.save_model(ov_model, './FP16/' + model_name + '.xml', compress_to_fp16=True)

# shutil.rmtree(converted_path)
# os.remove(f"{model_name}.pt")



# here want all fp32 16 to be inside below folder

# model_dir = "dlstreamer_omz/models/yolo11s"




from ultralytics import YOLO
import openvino, sys, shutil, os

# -------------------------------
# Configuration
# -------------------------------
model_name = 'yolo11s'
model_type = 'yolo_v11'

model_name = 'yolov8s'
model_type = 'yolo_v8'


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
