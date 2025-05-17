#!/usr/bin/env python3
import cv2
import numpy as np
from ultralytics import YOLO
import time
import os
import sys

def check_model_exists():
    """Check if YOLOv8 model exists, download if not"""
    model_path = "models/yolov8n.pt"
    
    # Create models directory if it doesn't exist
    if not os.path.exists("models"):
        os.makedirs("models")
        print("Created models directory")
    
    # Check if model exists, return path
    if os.path.exists(model_path):
        print(f"Found existing model at {model_path}")
        return model_path
    
    # If not in models folder, check in current directory
    if os.path.exists("yolov8n.pt"):
        print("Found model in current directory")
        return "yolov8n.pt"
    
    print("YOLOv8 model not found. It will be downloaded automatically when the script runs.")
    return "yolov8n.pt"  # Default model path that YOLO will download automatically

def main():
    try:
        # Get model path
        model_path = check_model_exists()
        
        # Load the YOLOv8 model
        print("Loading YOLO model...")
        model = YOLO(model_path)
        print("Model loaded successfully")
        
        # Open the webcam
        print("Opening webcam...")
        cap = cv2.VideoCapture(0)
        
        # Check if the webcam is opened correctly
        if not cap.isOpened():
            print("Error: Cannot open webcam")
            return
        
        # Get the current width and height
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(f"Webcam resolution: {width}x{height}")
        
        print("Webcam opened successfully")
        print("Press 'q' to quit")
        
        # Set up for FPS calculation
        prev_time = time.time()
        frame_count = 0
        
        while True:
            # Read a frame from the webcam
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image from webcam")
                break
            
            # Calculate FPS
            frame_count += 1
            current_time = time.time()
            if (current_time - prev_time) >= 1.0:
                fps = frame_count / (current_time - prev_time)
                frame_count = 0
                prev_time = current_time
            else:
                fps = frame_count / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
            
            try:
                # Run YOLOv8 inference on the frame
                results = model(frame)
                
                # Visualize the results on the frame
                annotated_frame = results[0].plot()
                
                # Display FPS
                cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                # Display the annotated frame
                cv2.imshow("YOLOv8 Webcam Detection", annotated_frame)
            except Exception as e:
                print(f"Error processing frame: {e}")
                # Display the original frame if processing fails
                cv2.putText(frame, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("YOLOv8 Webcam Detection", frame)
            
            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam and close all windows
        cap.release()
        cv2.destroyAllWindows()
        print("Webcam released and windows closed")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":
    print("Starting YOLOv8 Webcam Detection...")
    main()
    print("Program ended")