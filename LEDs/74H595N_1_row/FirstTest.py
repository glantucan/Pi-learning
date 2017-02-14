#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO


DEF_WAIT = 0.1
DATA = 13
RCLK = 19 # The output clock
SRCLK = 26 # The input clock
OE = 20 # Output enabled (LOW is enabled)
SRCLR = 21 # Shift register clear (LOW erases the memory)
 
def main():
	try:
		print("Preparing GPIO")
		init()
		
		shiftValue(1)
		shiftValue(1)
		shiftValue(0)
		shiftValue(1)
		showOutput()
		
		time.sleep(5)
		
		exitAndCleanUp()
		
	except KeyboardInterrupt:
		exitAndCleanUp()
		
	return 0
	
def shiftValue(val):
	GPIO.output(DATA, val)
	GPIO.output(SRCLK, GPIO.HIGH)
	# We need to put the input clock again to LOW so the next value 
	# can be shifted
	time.sleep(DEF_WAIT)
	GPIO.output(SRCLK, GPIO.LOW)
	
def showOutput():
	GPIO.output(RCLK, GPIO.HIGH)
	
def init():
	initGPIO()
	setOutputEnabled(True)
	resetRegisterMemory()	
	
def exitAndCleanUp():
	print('Exit & Clean up!')
	resetRegisterMemory()
	#Set the OE pin to HIGH to deactivate output
	setOutputEnabled(False)
	# Erase the memory before we go
	resetRegisterMemory()
	# Show the emptied memory so the LEDS are all shut down
	showOutput()
	GPIO.cleanup()	

def setOutputEnabled(val):
	# As the output is enabled for a LOW value
	GPIO.output(OE, not val)
		
def resetRegisterMemory():
	# Put the clocks to low
	GPIO.output(RCLK, GPIO.LOW)
	GPIO.output(SRCLK, GPIO.LOW)
	# Erase the memory by setting the SRCLR to LOW
	GPIO.output(SRCLR, GPIO.LOW)
	time.sleep(DEF_WAIT)
	GPIO.output(SRCLR, GPIO.HIGH)
	
def initGPIO():
	GPIO.setmode(GPIO.BCM)
	# Configure all used pins for output
	GPIO.setup(DATA, GPIO.OUT)
	GPIO.setup(SRCLK, GPIO.OUT)
	GPIO.setup(RCLK, GPIO.OUT)
	GPIO.setup(OE, GPIO.OUT)
	GPIO.setup(SRCLR, GPIO.OUT)

if __name__ == '__main__':
	main()
	
