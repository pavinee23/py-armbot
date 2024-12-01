from adafruit_servokit import ServoKit
import time

servo_channel = 0

kit = ServoKit(channels=16)

def open_gripper():
    kit.servo[servo_channel].angle = 0
    time.sleep(2)  # Allow time for the servo to move to position
    detach_servo()

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
        time.sleep(4.5)

        print("Closing gripper...")
        close_gripper()
        time.sleep(4.5)

    except KeyboardInterrupt:
        print("Program interrupted...")

    finally:
        close_gripper()
        print("Closed")
