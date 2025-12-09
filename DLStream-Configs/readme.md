# **YOLO → OpenVINO Converter (FP32 & FP16)**

This script converts **Ultralytics YOLO models (`.pt`)** into **OpenVINO IR format** and saves them neatly inside:

```
dlstreamer_omz/models/<model_name>/FP32/
dlstreamer_omz/models/<model_name>/FP16/
```

It automatically:
✔ Loads the YOLO model
✔ Exports to OpenVINO IR
✔ Assigns model metadata
✔ Saves FP32 & FP16
✔ Cleans temporary files

---

## **📦 Recommended Environment (Conda)**

It is strongly recommended to run this script inside a clean **conda environment** to avoid dependency conflicts.

### **1️⃣ Create Env**

```bash
conda create -n ov python=3.10 -y
conda activate ov
```

### **2️⃣ Install Required Packages**

```bash
pip install ultralytics openvino-dev
```

---

## **🛠 How to Use**

1. Place your YOLO model file in the same directory:

```
yolo11s.pt
```

(or modify the script’s `model_name` field)

2. Run the script:

```bash
python3 download_YOLO_models.py
```

---

## **📁 Output Folder Structure**

After running, you will see:

```
dlstreamer_omz/
└── models/
    └── yolo11s/
        ├── FP32/
        │   ├── yolo11s.xml
        │   └── yolo11s.bin
        └── FP16/
            ├── yolo11s.xml
            └── yolo11s.bin
```

✔ FP32 → Full precision (default for accuracy)
✔ FP16 → Half precision (recommended for CPU/GPU performance)

---

## **📝 Supported Model Types**

Modify at the top of the script:

```python
model_name = 'yolo11s'
model_type = 'yolo_v11'        # YOLOv11 detection
```

For segmentation:

```python
model_type = 'yolo_v11_seg'
```

The script automatically adds correct metadata for `boxes` / `masks`.

---

## **🧹 Cleanup Done Automatically**

The script removes:

* Temporary exported directory
* Original `.pt` file after successful conversion

---

## **❗ If You See Errors**

* Check that your `.pt` file name matches `model_name`
* Ensure OpenVINO dev is installed:

  ```bash
  pip install openvino-dev
  ```
* Ensure Python version is 3.8–3.12 in your conda env

---

