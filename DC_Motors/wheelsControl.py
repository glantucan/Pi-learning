#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

import os
import time
import sys

def pwm(pin, power):
    '''
    Uses pi-blaster command line tool to set the pwm specified
    duty-cycle (power from 0 to 1) to the desired pin (BCM format) 
    '''
    cmd = 'echo "' + str(pin) + '=' + str(power) + '" > /dev/pi-blaster'
    os.system(cmd)

def pwmRelease(pin):
    '''
    Release a pin so it can be used as digital GPIO or an input
    '''
    cmd = 'echo "' + str(pin) + '=0" > /dev/pi-blaster'
    cmd = 'echo "release ' + str(pin) + '"  > /dev/pi-blaster'
    os.system(cmd)


GPIO.setmode(GPIO.BCM) # Set GPIO numbers by BCM references

# Define the pins to be used for the inputs in the motor controller

# Right side wheels
enA = 18
#GPIO.setup(enA, GPIO.OUT)
#GPIO.output(enA, 0)
in1 = 27
GPIO.setup(in1, GPIO.OUT)
GPIO.output(in1, 0)
in2 = 22
GPIO.setup(in2, GPIO.OUT)
GPIO.output(in2, 0)
# Left side wheels
enB = 19
GPIO.setup(enB, GPIO.OUT)
GPIO.output(enB, 0)
in3 = 20
GPIO.setup(in3, GPIO.OUT)
GPIO.output(in3, 0)
in4 = 21
GPIO.setup(in4, GPIO.OUT)
GPIO.output(in4, 0)

def exitAndCleanUp():
    #GPIO.output(enA, 0)
    pwmRelease(enA)
    GPIO.output(enB, 0)
    GPIO.output(in1, 0)
    GPIO.output(in2, 0)
    GPIO.output(in3, 0)
    GPIO.output(in4, 0)
    print('Cleanup!')
    GPIO.cleanup()


try:
    # right wheels forward
    pwm(enA, 0.3)
    #GPIO.output(enA, 1)
    GPIO.output(in1, 1)
    time.sleep(2)
    GPIO.output(in1, 0)

    # right wheels backwaards
    GPIO.output(in2, 1)
    time.sleep(2)
    GPIO.output(in2, 0)


    # left wheels forward
    GPIO.output(enB, 1)
    GPIO.output(in4, 1) # instead of 3 because motors are inverted
    time.sleep(2)
    GPIO.output(in4, 0)

    # left wheels backwaards
    GPIO.output(in3, 1)
    time.sleep(2)
    GPIO.output(in3, 0)
    exitAndCleanUp()
    
except KeyboardInterrupt:
    exitAndCleanUp()
