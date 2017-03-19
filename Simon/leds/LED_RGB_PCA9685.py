#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import math
import RPi.GPIO as GPIO
# Import the PCA9685 module. Needs to obe installed 
# (sudo pip3 install adafruit-pca9685)
import Adafruit_PCA9685
# Import wiringpi. Needed if you want submilisecond intervals 
# i.e. wiringpi.delayMicroseconds(100)
# To install follow this instructions: https://github.com/Gadgetoid/WiringPi2-Python
#import wiringpi 
#import time


# Assumes common cathode configuration
class LED_RGB_PCA9685:

	def __init__(self, freq, rChannel, gChannel, bChannel):
		self.__rCh = rChannel
		self.__gCh = gChannel
		self.__bCh = bChannel
		self.__freq = freq
		# Give public access to the adafruit library
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(freq)
		self.__r = 0
		self.__g = 0
		self.__b = 0

	def setColor(self, r, g, b):
		self.__r = r
		self.__g = g
		self.__b = b
		self.pwm.set_pwm(self.__rCh, 0, r)
		self.pwm.set_pwm(self.__gCh, 0, g)
		self.pwm.set_pwm(self.__bCh, 0, b)

	# Properties
	@property
	def r(self):
		return self.__r
	@r.setter
	def r(self, r):
		self.__r = r

	@property
	def g(self):
		return self.__g
	@r.setter
	def g(self, g):
		self.__g = g

	@property
	def b(self):
		return self.__b
	@r.setter
	def b(self, b):
		self.__b = b


if (__name__ == "__main__"):
	try:
		led1 = LED_RGB_PCA9685(1500, 2, 1, 0)
		led1.setColor(1000, 0, 0)
	finally:
		led1.setColor(0, 0, 0)
		GPIO.cleanup()