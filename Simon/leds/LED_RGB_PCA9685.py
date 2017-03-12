#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import math
import RPi.GPIO as GPIO
# Import the PCA9685 module.
import Adafruit_PCA9685

frequency = 60

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency.
pwm.set_pwm_freq(frequency)


	
counter = 0
counterG = 0
counterB = 0
deg2rad = math.pi/180
while True:
	B = int(math.floor(math.sin((counter*1.1 + 0) * deg2rad) * 1800) + 1800)
	G = int(math.floor(math.sin((counter*1.2 + 60) * deg2rad) * 1800) + 1800)
	R = int(math.floor(math.sin((counter*1.3 + 120) * deg2rad) * 2000) + 2000)
	pwm.set_pwm(0, 0, B)
	pwm.set_pwm(1, 0, G)
	pwm.set_pwm(2, 0, R)
	time.sleep(0.0001)
	counter += 1
	
