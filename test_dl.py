import subprocess
import time

# --------------------------------------------
# MANUALLY LIST FILES YOU WANT TO RUN
# --------------------------------------------
FILES_TO_RUN = [
    "DLStream-Python/hello_dlstreamer.py",
    "DLStream-Python/dlstreamer_test_yolo.py",
    "DLStream-Python/dlstreamer_test_yolo_save_vid.py"
]

# Arguments you want to pass to every script
COMMON_ARGS = [
    "/home/dlstreamer/inputs/head-pose-face-detection-female-and-male.mp4",
    "/home/dlstreamer/DLStream-Configs/dlstreamer_omz/models/yolov8s/FP16/yolov8s.xml"
]

def main():
    for file in FILES_TO_RUN:
        print(f"\n==============================")
        print(f" RUNNING: {file}")
        print(f"==============================")

        try:
            subprocess.run(["python3", file] + COMMON_ARGS, check=True)
        except subprocess.CalledProcessError:
            print(f"❌ ERROR while running {file}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        # 🔥 Add 5-second delay here
        print("⏳ Waiting for 5 seconds before next file...\n")
        time.sleep(5)

if __name__ == "__main__":
    main()