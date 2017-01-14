#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

import time
import sys


GPIO.setmode(GPIO.BCM) # Set GPIO numbers by BCM references

# Define the pins to be used for the inputs in the motor controller

# Right side wheels
enA = 17
GPIO.setup(enA, GPIO.OUT)
GPIO.output(enA, 0)
in1 = 27
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, 0)
in2 = 22
GPIO.setup(in2, GPIO.OUT)
GPIO.output(in2, 0)
# Left side wheels
enB = 16
GPIO.setup(enB, GPIO.OUT)
GPIO.output(enB, 0)
in3 = 20
GPIO.setup(in3, GPIO.OUT)
GPIO.output(in3, 0)
in4 = 21
GPIO.setup(in4, GPIO.OUT)
GPIO.output(in4, 0)


			

def exitAndCleanUp():
	GPIO.output(enA, 0)
	GPIO.output(enB, 0)
	GPIO.output(in1, 0)
	GPIO.output(in2, 0)
	GPIO.output(in3, 0)
	GPIO.output(in4, 0)
	print('Cleanup!')
	GPIO.cleanup()	


try:
    # right wheels forward
    GPIO.output(in1, 1)
    time.sleep(2)
    GPIO.output(in1, 1)
	exitAndCleanUp()
	
except KeyboardInterrupt:
	exitAndCleanUp()







