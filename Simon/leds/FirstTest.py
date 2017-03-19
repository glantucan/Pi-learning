#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import math
import RPi.GPIO as GPIO
# Import the PCA9685 module.
import Adafruit_PCA9685
import wiringpi

frequency = 1500

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Set frequency.
pwm.set_pwm_freq(frequency)

rMax = 100
gbMax = 90
	
counter = 0
deg2rad = math.pi/180
while True:
	B1 = int(math.floor(math.sin((counter*10*1.1 + 0) * deg2rad) * gbMax) + gbMax)
	G1 = int(math.floor(math.sin((counter*10*1.2 + 0) * deg2rad) * gbMax) + gbMax)
	R1 = int(math.floor(math.sin((counter*10*1.3 + 0) * deg2rad) * rMax) + rMax)
	B2 = int(math.floor(math.sin((counter*10*1.1 + 30) * deg2rad) * gbMax) + gbMax)
	G2 = int(math.floor(math.sin((counter*10*1.2 + 30) * deg2rad) * gbMax) + gbMax)
	R2 = int(math.floor(math.sin((counter*10*1.3 + 30) * deg2rad) * rMax) + rMax)
	B3 = int(math.floor(math.sin((counter*10*1.1 + 60) * deg2rad) * gbMax) + gbMax)
	G3 = int(math.floor(math.sin((counter*10*1.2 + 60) * deg2rad) * gbMax) + gbMax)
	R3 = int(math.floor(math.sin((counter*10*1.3 + 60) * deg2rad) * rMax) + rMax)
	B4 = int(math.floor(math.sin((counter*10*1.1 + 90) * deg2rad) * gbMax) + gbMax)
	G4 = int(math.floor(math.sin((counter*10*1.2 + 90) * deg2rad) * gbMax) + gbMax)
	R4 = int(math.floor(math.sin((counter*10*1.3 + 90) * deg2rad) * rMax) + rMax)
	pwm.set_pwm(0, 0, B1)
	pwm.set_pwm(1, 0, G1)
	pwm.set_pwm(2, 0, R1)
	pwm.set_pwm(4, 0, B2)
	pwm.set_pwm(5, 0, G2)
	pwm.set_pwm(6, 0, R2)
	pwm.set_pwm(8, 0, B3)
	pwm.set_pwm(9, 0, G3)
	pwm.set_pwm(10, 0, R3)
	pwm.set_pwm(12, 0, B4)
	pwm.set_pwm(13, 0, G4)
	pwm.set_pwm(14, 0, R4)
	#time.sleep(0.01)
	wiringpi.delayMicroseconds(100)
	counter += 1