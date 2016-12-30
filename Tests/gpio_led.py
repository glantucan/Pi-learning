#!/usr/bin/env/ python
import RPi.GPIO as GPIO

import time

LedPin = 11 # physical number correponding to GPIO0 (GPIO17)

GPIO.setmode(GPIO.BOARD) # Set GPIO numbers by physical location
GPIO.setup(LedPin, GPIO.OUT) # Set LedPin's mode as output
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin as high (3.3V) to turn off the led

	
try:
	while True:
		print ('...led on')
		GPIO.output(LedPin, GPIO.LOW)  # led on
		
		time.sleep(0.15)	
			
		print ('...led off')
		GPIO.output(LedPin, GPIO.HIGH)  # led off
		
		time.sleep(0.15)
		
except KeyboardInterrupt:
	GPIO.output(LedPin, GPIO.HIGH)
	GPIO.cleanup()
