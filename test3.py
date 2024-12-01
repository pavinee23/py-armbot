from adafruit_servokit import ServoKit
import time
from picamera2 import Picamera2
import cv2
import numpy as np










kit = ServoKit(channels=16)
kit.servo[9].angle = 60
time.sleep(2.5)
kit.servo[9].angle = 80
time.sleep(2.5)
kit.servo[9].angle = 70
time.sleep(2.5)
kit.servo[5].angle = 0
time.sleep(2.5)

servo_channel = 0
def open_gripper():
    kit.servo[servo_channel].angle = 0
    time.sleep(2.5)  # Allow time for the servo to move to position
    detach_servo()
    
    
    time.sleep(2.5)
    kit.servo[5].angle = 150
    time.sleep(2.5)
    kit.servo[5].angle = 90
    time.sleep(2.5)
    kit.servo[5].angle = 40
  
 

def close_gripper():
    kit.servo[servo_channel].angle = 90
    time.sleep(2)  # Allow time for the servo to move to position
    detach_servo()

def detach_servo():
    kit.servo[servo_channel].angle = None  # Setting the angle to None to detach the signal



if __name__ == "__main__":
    try:
        print("Opening gripper...")
        open_gripper()
        time.sleep(1.5)

        print("Closing gripper...")
        close_gripper()
        time.sleep(2.5)

    except KeyboardInterrupt:
        print("Program interrupted...")

    finally:
        close_gripper()
        print("Closed")


        time.sleep(2.5)
        kit.servo[5].angle = 90
        time.sleep(2.5)
        kit.servo[9].angle = 110
        time.sleep(2.5)
        kit.servo[9].angle = 180
        time.sleep(2.5)


def open_gripper1():
    kit.servo[servo_channel].angle = 90
    time.sleep(2.5)  # Allow time for the servo to move to position
    detach_servo()
    time.sleep(2.5)
    kit.servo[5].angle = 150
       
    
if __name__ == "__main__":
    try:
        print("Opening gripper1...")
        open_gripper1()
        time.sleep(1)


    finally:
        open_gripper()
        time.sleep(2.5)
        kit.servo[5].angle = 90
        print("End")
 
 
