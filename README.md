
# <br> <img src="https://media0.giphy.com/media/J19OSJKmqCyP7Mfjt1/giphy.gif" width="80" height="30" /> **Intel DLStreamer – Ultra-Optimized AI Video Analytics Stack (OpenVINO Powered)**

### 🔖 *EXCLUSIVE Release – Low-Code • Hardware-Accelerated • Docker-Ready*


<p align="center">
  <p align="center"><img width="70%" src="demo.gif"></p>
</p>

<p align="center">
  <b>orchestrator-ready code for seamless integration</b><br>
  <b>YOLO Detection • YOLO Pose • Tracking • ROI Analytics • Multi-Stream Pipelines • Python First</b><br>
  <b>Fully Accelerated · Low Code · Docker Ready · Production Tested</b>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Intel-DLStreamer-blue?style=for-the-badge&logo=intel"/>
<img src="https://img.shields.io/badge/OpenVINO-2024.4+-blue?style=for-the-badge&logo=openvino"/>
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/Ubuntu-24.04-orange?style=for-the-badge&logo=ubuntu"/>
<img src="https://img.shields.io/badge/CPU/VPU/GPU-XPU%20Ready-green?style=for-the-badge&logo=intel"/>
</p>

---



# 🖥 **Recommended System Setup**

| Component              | Recommended / Supported                                                         |
| ---------------------- | ------------------------------------------------------------------------------- |
| **OS**                 | **Ubuntu 24.04 LTS**                                                            |
| **OpenVINO Version**   | **2025.4+**                                                                     |
| **DLStreamer Version** | **2025.0.1.3**                                                                        |
| **Acceleration**       | **Intel CPU • iGPU • Intel ARC • Myriad-X VPU • Neural Compute Stick 2 (NCS2)** |
|                        | **Luxonis OAK Series (vPU offload)**                                            |
|                        | **GNA / HAILO / OpenVINO EP Devices**                                           |
| **Docker Support**     | Yes – OpenVINO Runtime Containers                                               |
| **Bare Metal Support** | Full                                                                            |

✔️ **Supports full XPU execution (CPU + GPU + VPU)**
✔️ **OAK-D / OAK-Lite / OAK-Pro support (DepthAI + OpenVINO backend)**
✔️ **Movidius MyriadX / NCS2 optimized**
✔️ **Multi-stream, multi-model, ROI pipelines**
✔️ **Python & C++**

---

# 🤖 **Supported OpenVINO Hardware**

### **Intel CPUs**

* 11th/12th/13th/14th Gen Intel Core
* Intel Xeon scalable
* Intel Atom (Edge)

### **Intel Integrated GPUs**

* Intel UHD / Iris / Iris Xe
* Intel Xe-LP / Xe-HPG
* Tiger Lake, Alder Lake, Raptor Lake, Meteor Lake iGPU

### **Intel ARC Discrete GPUs**

* ARC A380 / A750 / A770
* ARC Pro Series

### **Intel® Data Center GPUs**



---


# ⚡ **Quick Start (1 Step)**

**Install OpenVINO runtime → Clone repo → Run QuickTest.sh**

---

## Install OpenVINO + DLStreamer

Intel official quick install:

🔗 [https://docs.openvino.ai](https://docs.openvino.ai)

DLStreamer:

🔗 [https://dlstreamer.github.io/get_started](https://github.com/open-edge-platform/edge-ai-libraries/tree/main/libraries/dl-streamer))

---

## Clone this Repo and Run Quick Demo

```bash
git clone https://github.com/bharath5673/DLstream.git
cd DLstream
bash QuickDemo.sh
```

Runs instantly with DLStreamer-ready pipelines:

* YOLO Detection
* YOLO Pose
* Multi-model, multi-stream pipelines
* Region-based analytics
* Full OpenVINO acceleration
* **[YOLO Models Converter](https://github.com/bharath5673/DLstream/tree/main/DLStream-Configs)**

---

# 🎯 **What This Repo Provides**

### ✔️ **Docker-Ready**

Run the entire AI video analytics stack inside Intel's official:

* OpenVINO Runtime Containers
* DLStreamer Media Analytics Containers

All pipelines run **identical** in Docker and Bare-Metal.

---

### ✔️ **DLStreamer Templates (Production Ready)**

* Multi-model pipelines
* YOLO detection (OpenVINO IR / ONNX)
* YOLO-pose via OpenVINO
* Multi-stream tiled GStreamer pipelines
* Region-based analytics
* Python GStreamer bindings
* ❗C++ full application templates
* Triton-compatible (OpenVINO backend)

---

### ✔️ **Fully-Optimized & Low-Code**

Minimal coding — **edit configs and run**.

You get:

* HIGH throughput using XPU execution
* ZERO CUDA / NVIDIA dependencies
* End-to-end pipelines optimized for CPU+iGPU

---

# 🌟 **Showcase Gallery**

### 🔥 Multi-Model Pipeline

<p align="center"><img width="70%" src="https://user-images.githubusercontent.com/33729709/210167600-6a677a62-40ee-4afa-b484-d0d56e78e230.gif"></p>

🔗 `DLStreamer-Configs/MultiModel`

---

### 🟦 ROI Based Counting (Python)

<p align="center"><img width="70%" src="https://user-images.githubusercontent.com/33729709/211142186-a9ecd225-4f90-4310-91df-862e243f8833.gif"></p>

🔗 `DLStreamer-Python/ROI-counting`

---

### 🟧 YOLO POSE (OpenVINO)

<p align="center"><img width="70%" src="https://github.com/bharath5673/DLstream/blob/main/demo/human_pose_estimation.gif"></p>

🔗 `DLStreamer-Python/Pose/`

---
### 🟧 YOLO PERSON TRACKING (OpenVINO)

<p align="center"><img width="70%" src="https://github.com/bharath5673/DLstream/blob/main/demo/pedestrian_tracker.gif"></p>

🔗 `DLStreamer-Python/tracking/`

---
### 🟧  SEGMENTATION

<p align="center"><img width="70%" src="https://github.com/bharath5673/DLstream/blob/main/demo/segmentation.gif"></p>

🔗 `DLStreamer-Python/Pose/`

---
### 🟧  Face ANALYSIS

<p align="center"><img width="70%" src="https://github.com/bharath5673/DLstream/blob/main/demo/interactive_face_detection.gif"></p>

🔗 `DLStreamer-Python/face/`

---
### 🟧  CLASSIFICATION

<p align="center"><img width="70%" src="https://github.com/bharath5673/DLstream/blob/main/demo/classification.gif"></p>

🔗 `DLStreamer-Python/classification/`

---


### ⚡ Quick Demo

```bash
cd DLstream
bash QuickDemo.sh
```

---

# 📂 **Repo Structure**

```
DLstreamer/
├── demo
│   ├── pedestrian_tracker.gif
│   ├── segmentation.gif
├── demo.gif
├── DLStream-Configs
│   ├── dlstreamer_omz
│   │   ├── models
│   │   │   ├── intel
│   │   │   │   ├── age-gender-recognition-retail-0013
│   │   │   │   │   ├── FP16
│   │   │   │   │   │   ├── age-gender-recognition-retail-0013.bin
│   │   │   │   │   │   └── age-gender-recognition-retail-0013.xml
│   │   │   │   │   ├── FP16-INT8
│   │   │   │   │   │   ├── age-gender-recognition-retail-0013.bin
│   │   │   │   │   │   └── age-gender-recognition-retail-0013.xml
│   │   │   │   │   └── FP32
│   │   │   │   │       ├── age-gender-recognition-retail-0013.bin
│   │   │   │   │       └── age-gender-recognition-retail-0013.xml
│   │   │   │   ├── emotions-recognition-retail-0003
│   │   │   │   │   ├── FP16
│   │   │   │   │   │   ├── emotions-recognition-retail-0003.bin
│   │   │   │   │   │   └── emotions-recognition-retail-0003.xml
│   │   │   │   │   ├── FP16-INT8
│   │   │   │   │   │   ├── emotions-recognition-retail-0003.bin
│   │   │   │   │   │   └── emotions-recognition-retail-0003.xml
│   │   │   │   │   └── FP32
│   │   │   │   │       ├── emotions-recognition-retail-0003.bin
│   │   │   │   │       └── emotions-recognition-retail-0003.xml

│   │   │   ├── yolo11n_openvino_model
│   │   │   │   ├── n
│   │   │   │   │   ├── metadata.yaml
│   │   │   │   │   ├── yolo11n.bin
│   │   │   │   │   ├── yolo11n.json
│   │   │   │   │   └── yolo11n.xml
│   │   │   │   ├── yolo11s.bin
│   │   │   │   └── yolo11s.xml
│   │   │   ├── yolo11n.pt
│   │   │   ├── yolo11s
│   │   │   │   ├── FP16
│   │   │   │   │   ├── yolo11s.bin
│   │   │   │   │   └── yolo11s.xml
│   │   │   │   └── FP32
│   │   │   │       ├── yolo11s.bin
│   │   │   │       └── yolo11s.xml

│   │   ├── openvino_ga_cid
│   │   └── stats
│   └── download_YOLO_models.py
├── DLStream-Python
│   ├── dlstreamer_test_yolo.py
│   ├── dlstreamer_test_yolo_save_vid.py
│   ├── draw_face_attributes.py
│   └── hello_dlstreamer.py
├── inputs
│   ├── 1192116-sd_640_360_30fps.mp4
│   ├── head-pose-face-detection-female-and-male.mp4
│   └── youtube_stream_20250321_151616.mp4
├── Intel_logo.jpg
├── OpenVino.png
├── outputs
│   └── dlstream_output_20251209_072421.mp4
├── QuickDemo.sh                                                   ### main sh file
├── README.md
└── test_dl.py                                                     ### orchestartor running all python demos

```

---

# 🙏 **Acknowledgements**

<p align="center">
  <img src="https://github.com/bharath5673/DLstream/blob/main/Intel_logo.jpg" height="55"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://github.com/bharath5673/DLstream/blob/main/OpenVino.png" height="55"/> <!-- OpenVINO -->
  &nbsp;&nbsp;&nbsp;
  <img src="https://opencv.org/wp-content/uploads/2020/07/OpenCV_logo_black.png" height="55"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" height="55"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://www.cnx-software.com/wp-content/uploads/2019/12/MediaPipeLogo.png" height="65"/>
</p>

<p align="center">
<b>Massive respect to the Intel Edge AI + OpenVINO community.</b><br>
<i>Pipelines, models, tracking logic, and deployment flows are inspired by best practices from DLStreamer and open-source AI/ML communities.</i>
</p>

---

## 🔰 **Credits & Sources**

<details>
<summary><b>🟩 YOLO Ecosystem</b></summary><br>

* [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)
* [https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose](https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose)
* OpenVINO YOLO models: [https://docs.openvino.ai](https://docs.openvino.ai)

</details>

---

<details>
<summary><b>🟦 Core AI / CV Architectures</b></summary><br>

* OpenVINO Model Zoo
* OpenCV DNN
* RepVGG, OREPA, FasterRCNN/SSD papers
* ONNX Runtime → OpenVINO conversion tools

</details>

---

<details>
<summary><b>🟧 Intel DLStreamer & Media Analytics</b></summary><br>

* DLStreamer (gst-gva)
* OpenVINO Execution Provider
* GStreamer plugins for inference (`gvadetect`, `gvaclassify`, `gvatrack`, etc.)

Documentation:
[https://dlstreamer.github.io](https://dlstreamer.github.io)
[https://docs.openvino.ai](https://docs.openvino.ai)

</details>

---

<details>
<summary><b>🔵 Tracking, ROI, Multi-Model Inspirations</b></summary><br>

* KLT + ByteTrack/DeepSORT concepts
* GVA ROI analytics
* Open-source MOT community

</details>

---

## ⭐ **Special Thanks**

<p align="center">
Thank you to every engineer and researcher contributing to<br>
OpenVINO, DLStreamer, YOLO, tracking algorithms, and computer vision innovation.
</p>

<p align="center"><b>This project stands on the shoulders of giants.</b></p>


