#!/bin/bash

# Create models directory if it doesn't exist
mkdir -p models

# Download YOLOv3-tiny weights if they don't exist
if [ ! -f "models/yolov3-tiny.weights" ]; then
    echo "Downloading YOLOv3-tiny weights..."
    curl -L https://pjreddie.com/media/files/yolov3-tiny.weights -o models/yolov3-tiny.weights
    echo "Download complete!"
else
    echo "YOLOv3-tiny weights already exist."
fi

# Download YOLOv3-tiny config if it doesn't exist
if [ ! -f "models/yolov3-tiny.cfg" ]; then
    echo "Downloading YOLOv3-tiny config..."
    curl -L https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg -o models/yolov3-tiny.cfg
    echo "Download complete!"
else
    echo "YOLOv3-tiny config already exists."
fi

# Create COCO names file if it doesn't exist
if [ ! -f "models/coco.names" ]; then
    echo "Creating COCO names file..."
    python -c "
import os
coco_path = 'models/coco.names'
class_names = [
    'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 
    'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 
    'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 
    'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 
    'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 
    'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 
    'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]
with open(coco_path, 'w') as f:
    f.write('\n'.join(class_names))
print('Created COCO class names file')
"
else
    echo "COCO names file already exists."
fi

echo "All required files are now available. You can now run: python webcam_detection.py"