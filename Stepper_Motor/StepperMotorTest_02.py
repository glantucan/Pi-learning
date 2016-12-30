#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

## TODO: Support for negative angles

#import RPi.GPIO as GPIO

import time
import sys


#GPIO.setmode(GPIO.BCM) # Set GPIO numbers by BCM references

# Define the pins to be used for the inputs in the motor controller
controlPins = [4, 17, 27, 22]

# Set thos pins to output mode
for pin in controlPins:
	print ("Setting pin " + str(pin) + " to OUTPUT mode")
#	GPIO.setup(pin, GPIO.OUT)
#	GPIO.output(pin, 0)
	
# Define the array of step arrays for half stepping
seq = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]

lastHalfStep = 0
stepDuration = 0.001

def rotateSteps(steps, clockwise): 
	
	global lastHalfStep
	delayedSteps = 0
	steps += lastHalfStep
	if steps > 8:
		delayedSteps = steps - 8
		steps = 8
		
	for halfstep in range(lastHalfStep, steps, 1): # Complete sequence of halfsteps = 0.703 deg
		# Set the pins for each halfstep
		#print(str(halfstep))
		for pin in range(4):
		# Set each pin
			#GPIO.output(controlPins[pin], seq[halfstep][pin])
			print()
		print(str(halfstep) + ': ' +','.join(str(x) for x in seq[halfstep]) )
		time.sleep(stepDuration)
		lastHalfStep = halfstep + 1
	if delayedSteps > 0:
		lastHalfStep = 0
		#print("recursive call")	
		if (delayedSteps<0):
			rotateSteps(delayedSteps, False)
		else:
			rotateSteps(delayedSteps, True)

def rotateCycles(cycles): 
	min = 0
	max = cycles
	incr = 1
	steps = 8
	if (cycles < 0):
		min = cycles
		max = 0
		incr = 1
		steps = -8
	for i in range(min, max, incr): # full revolution = 512 cycles of all steps
		if (steps<0):
			rotateSteps(steps, False)
		else:
			rotateSteps(steps, True)
		print(i)

def rotate(angle):
	cycleAngle = 360 / 512
	stepAngle = cycleAngle / 8
	cycles = int(angle / cycleAngle)
	angleRest = angle - cycles * cycleAngle
	remainingSteps = int(angleRest / stepAngle)
	
	
	# print("cycleAngle: " + str(cycleAngle))
	# print("stepAngle: " + str(stepAngle))
	print("cycles: " + str(cycles))
	print("reproduced angle: " + str(cycles * cycleAngle))
	print("angleRest: " + str(angleRest))
	print("remainingSteps: " + str(remainingSteps))

	rotateCycles(cycles)
	if (remainingSteps<0):
		rotateSteps(remainingSteps, False)
	else:
		rotateSteps(remainingSteps, True)
	print(i)

			

def exitAndCleanUp():
	for pin in controlPins:
#		GPIO.setup(pin, GPIO.OUT)
#		GPIO.output(pin, 0)
		print('Cleanup!')
#	GPIO.cleanup()	


try:
	if len(sys.argv) > 1:
		for i in range(1, len(sys.argv), 1):
			print("---> rotating " + str(sys.argv[i]) + " degrees")
			rotate(float(sys.argv[i]))
			time.sleep(0.5)
	exitAndCleanUp()
	
except KeyboardInterrupt:
	exitAndCleanUp()
