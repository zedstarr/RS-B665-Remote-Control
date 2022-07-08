import RPi.GPIO as GPIO
import os
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)

GPIO.output(24, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(24, GPIO.LOW)

