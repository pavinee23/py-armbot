from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
kit.servo[0].angle = 135
time.sleep(2.5)
kit.servo[0].angle = 155
time.sleep(2.5)
kit.servo[0].angle = 180
time.sleep(2.5)
kit.servo[0].angle = 155
time.sleep(2.5)
kit.servo[0].angle = 135
time.sleep(2.5)
kit.servo[0].angle = 155
