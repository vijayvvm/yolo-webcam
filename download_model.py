#!/usr/bin/env python3
import os
import requests
from tqdm import tqdm
import sys

def download_file(url, destination):
    """
    Download a file from a URL to a destination with a progress bar
    """
    if os.path.exists(destination):
        print(f"Model already exists at {destination}")
        return
        
    print(f"Downloading YOLOv8 model from {url}")
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    
    with open(destination, 'wb') as f, tqdm(
            desc=destination,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
        for data in response.iter_content(block_size):
            size = f.write(data)
            bar.update(size)
    
    print(f"Downloaded model to {destination}")

def main():
    # Create models directory if it doesn't exist
    if not os.path.exists("models"):
        os.makedirs("models")
        print("Created models directory")
    
    # URL for YOLOv8n model
    model_url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt"
    model_path = "models/yolov8n.pt"
    
    # Download the model
    try:
        download_file(model_url, model_path)
        print("Download complete! You can now run the detection script.")
    except Exception as e:
        print(f"Error downloading model: {e}")
        print("\nIf download fails, you can manually download the model from:")
        print(f"  {model_url}")
        print(f"And save it to: {model_path}")
        print("\nAfter downloading, run: python3 webcam_detection.py")

if __name__ == "__main__":
    print("Starting model download...")
    main()