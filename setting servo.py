from adafruit_servokit import ServoKit
import time


kit = ServoKit(channels=16)


def move_servo(channel, angle):
    kit.servo[channel].angle = angle
    time.sleep(2.5)
    print(f"Servo {channel} is set to {angle} degrees")


move_servo(9, 0)


move_servo(9, 70)

move_servo(5, 50)


move_servo(5, 40)


move_servo(5, 30)

move_servo(5, 20)

