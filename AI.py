from imageai.Detection import ObjectDetection
import cv2
import serial
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# Initialize object detection
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
detector.loadModel()

# Initialize serial connection to the robotic arm
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Adjust to your port

# Initialize Raspberry Pi Camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Allow the camera to warm up
time.sleep(0.1)

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array

    # Detect objects in the image
    detections = detector.detectObjectsFromImage(input_image=image, input_type="array", output_type="array")[1]

    # Process detections
    for detection in detections:
        if detection["name"] == "person":  # Example: track a person
            x1, y1, x2, y2 = detection["box_points"]
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Send the coordinates to the robotic arm
            command = f"MOVE {center_x} {center_y}\n"
            ser.write(command.encode())

            # Draw bounding box and label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, detection["name"], (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image
    cv2.imshow("Object Tracking", image)

    # Clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # If 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.close()
cv2.destroyAllWindows()
ser.close()  (Object["percentage_probability"] )