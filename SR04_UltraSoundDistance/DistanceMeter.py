#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


TRIG = 13
ECHO = 26

print("Distance Measurement In Progress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    pulseStart = time.time()

while GPIO.input(ECHO) == 1:
    pulseEnd = time.time()

pulse_duration = pulseEnd - pulseStart

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance:", distance, "cm")

GPIO.cleanup()