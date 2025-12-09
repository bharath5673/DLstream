
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
| **OpenVINO Version**   | **2024.4+**                                                                     |
| **DLStreamer Version** | **1.8+**                                                                        |
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
* Fully supported via **OpenVINO GPU plugin**

### **Intel Movidius VPUs**

* **Myriad X VPU**
* **Intel Neural Compute Stick 2 (NCS2)**
* **DepthAI / Luxonis OAK devices (Myriad-X on board)**

  * OAK-D
  * OAK-Lite
  * OAK-Pro
  * OAK-FF
  * OAK-1/2 POE
  * OAK-SoM

### **Partner Accelerators (via OpenVINO EP)**

* **HAILO-8/10** (OpenVINO EP)
* **GNA v1/v2** (keyword spotting, speech models)

---


# ⚡ **Quick Start (1 Step)**

**Install OpenVINO runtime → Clone repo → Run QuickTest.sh**

---

## Install OpenVINO + DLStreamer

Intel official quick install:

🔗 [https://docs.openvino.ai](https://docs.openvino.ai)

DLStreamer:

🔗 [https://dlstreamer.github.io/get_started](https://dlstreamer.github.io/get_started)

---

## Clone this Repo and Run Quick Demo

```bash
git clone https://github.com/bharath5673/DLStreamer-OpenVINO.git
cd DLStreamer-OpenVINO
bash QuickDemo.sh
```

Runs instantly with DLStreamer-ready pipelines:

* YOLO Detection
* YOLO Pose
* Multi-model, multi-stream pipelines
* Region-based analytics
* Full OpenVINO acceleration

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

<p align="center"><img width="70%" src="pose_demo.gif"></p>

🔗 `DLStreamer-Python/Pose/`

---


### ⚡ Quick Demo

```bash
cd DLStreamer-OpenVINO
bash QuickDemo.sh
```

---

# 📂 **Repo Structure**

```
DLStreamer-OpenVINO/
│
├── DLStreamer-Configs/
│   ├── MultiModel/
│   ├── Streams/ (multi-stream, tiling, custom pipelines)
│
├── DLStreamer-Python/
│   ├── yolo
│   ├── yolo + pose
│   ├── ROI counting
│   ├── trajectory tracking
│
├── CNN-to-DLStreamer/
│
└── QuickTest.sh
```

---

# 🙏 **Acknowledgements**

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/64/Intel_logo_%282020%2C_dark_blue%29.svg" height="55"/>
  &nbsp;&nbsp;&nbsp;
  <img src="https://datatonic.com/insights/machine-learning-inference-intel-openvino" height="55"/> <!-- OpenVINO -->
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


