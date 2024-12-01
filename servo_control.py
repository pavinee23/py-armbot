from adafruit_servokit import ServoKit
import time


kit = ServoKit(channels=16)


def move_servo_and_check(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(1)
    print(f"Servo {channel} is set to {angle} degrees")


servo_channel = 5

for angle in range(0, 151, 10):
    move_servo_and_check(servo_channel, angle)


move_servo_and_check(servo_channel, 30)
