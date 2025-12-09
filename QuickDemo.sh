#!/bin/bash
set -e

# -----------------------------------
# CONFIG
# -----------------------------------
export DISPLAY=:1
xhost +

CONTAINER_NAME="dlstreamer-temp"
IMAGE_NAME="intel/dlstreamer:latest"

PROJECT_ROOT="./"

# Paths to copy
COPY_PATHS=(
    "$PROJECT_ROOT/DLStream-Configs"
    "$PROJECT_ROOT/DLStream-Python"
    "./inputs"
    "./outputs"
    "./test_dl.py"
)

# -----------------------------------
# REMOVE OLD CONTAINER
# -----------------------------------
docker rm -f $CONTAINER_NAME 2>/dev/null || true

echo "Creating container..."
docker create \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -e DISPLAY=$DISPLAY \
  --network host \
  --privileged \
  -w /home/dlstreamer \
  -v "$(pwd)/outputs:/home/dlstreamer/outputs" \
  --name $CONTAINER_NAME \
  $IMAGE_NAME sleep infinity

echo "Starting container..."
docker start $CONTAINER_NAME

# -----------------------------------
# COPY FILES INTO CONTAINER
# -----------------------------------
echo "Copying required project folders..."
for path in "${COPY_PATHS[@]}"; do
    docker cp "$path" "$CONTAINER_NAME:/home/dlstreamer/"
done

# -----------------------------------
# RUN MAIN TEST SCRIPT
# -----------------------------------

# docker exec -it $CONTAINER_NAME bash                                  ##debug

echo "Running test_dl.py..."
docker exec -it $CONTAINER_NAME python3 /home/dlstreamer/test_dl.py

echo "Running draw_face_attributes..."
docker exec -it "$CONTAINER_NAME" python3 /home/dlstreamer/DLStream-Python/draw_face_attributes.py \
                                  -i /home/dlstreamer/inputs/head-pose-face-detection-female-and-male.mp4 \
                                  -d /home/dlstreamer/DLStream-Configs/dlstreamer_omz/models/intel/face-detection-adas-0001/FP32/face-detection-adas-0001.xml \
                                  -c1 /home/dlstreamer/DLStream-Configs/dlstreamer_omz/models/intel/age-gender-recognition-retail-0013/FP32/age-gender-recognition-retail-0013.xml \
                                  -c2 /home/dlstreamer/DLStream-Configs/dlstreamer_omz/models/intel/emotions-recognition-retail-0003/FP32/emotions-recognition-retail-0003.xml \
                                  -c3 /home/dlstreamer/DLStream-Configs/dlstreamer_omz/models/intel/facial-landmarks-35-adas-0002/FP32/facial-landmarks-35-adas-0002.xml \
                                  -o display



# -----------------------------------
# CLEANUP
# -----------------------------------
echo "Cleaning up container..."
docker rm -f $CONTAINER_NAME

sudo chown -R $USER:$USER ./outputs

echo "Done!"
