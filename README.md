# YOLO Webcam Object Detection

A Python application that uses YOLOv8 to detect objects from your webcam feed in real-time.

## Setup with Python 3

This project requires Python 3 and uses the latest YOLOv8 model from Ultralytics.

### 1. Install Dependencies

```bash
cd yolo-webcam
python3 -m pip install -r requirements.txt
```

### 2. Download the YOLOv8 Model

You can download the model with:

```bash
python3 download_model.py
```

Alternatively, the model will be automatically downloaded when you first run the webcam detection script.

## Usage

Run the webcam detection script:

```bash
python3 webcam_detection.py
```

- Press 'q' to quit the application

## Features

- Real-time object detection using YOLOv8
- Automatic model download
- FPS counter
- User-friendly interface with bounding boxes and labels

## Requirements

- Python 3.6+
- OpenCV
- NumPy
- Ultralytics YOLOv8
- A working webcam

<img width="1122" alt="image" src="https://github.com/user-attachments/assets/1d4ce181-1b80-440c-bbd3-cd1c5444bf76" />
