import RPi.GPIO as GPIO
import os
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(22, GPIO.LOW)

