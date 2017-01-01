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
	time.sleep(0)
	#print("Setting pin " + str(pin) + " to OUTPUT mode")
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
generalStepCounter = 0
lastHalfStep = 0
stepDuration = 0.001

def rotateSteps(steps):
	print()
	global lastHalfStep
	global generalStepCounter
	delayedSteps = 0
	steps += lastHalfStep
	inc = 1 if steps > 0 else -1

	for halfstep in range(lastHalfStep, steps, inc): # Complete sequence of halfsteps = 0.703 deg
		# Set the pins for each halfstep
		#print(str(halfstep))
		curStep = halfstep % len(seq)
		for pin in range(4):
		# Set each pin
			#GPIO.output(controlPins[pin], seq[curStep][pin])
			time.sleep(0)
		print(str(generalStepCounter) + ', ' + str(curStep) + ': ' +','.join(str(x) for x in seq[curStep]) )
		time.sleep(stepDuration)
		lastHalfStep = curStep + inc
		generalStepCounter += inc


def rotate(angle):
	cycleAngle = 360 / 512
	stepAngle = cycleAngle / 8
	cycles = int(angle / cycleAngle)
	angleRest = angle - cycles * cycleAngle
	remainingSteps = int(round(angleRest / stepAngle))
	
	print("cycleAngle: " + str(cycleAngle))
	print("stepAngle: " + str(stepAngle))
	print("cycles: " + str(cycles))
	print("reproduced angle: " + str(cycles * cycleAngle))
	print("angleRest: " + str(angleRest))
	print("remainingSteps: " + str(remainingSteps))
	
	rotateSteps(cycles*8 + remainingSteps)

			

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
