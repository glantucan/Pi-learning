#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

import os
import time
import sys

class WheelsControl_L298N():
    def __init__(rightPins, leftPins):
        # Define the pins to be used for the inputs in the motor controller
        self.enA = rightPins[0]
        self.in1 = rightPins[1]
        self.in2 = rightPins[2]
        enB = leftPins[0]
        in3 = leftPins[1]
        in4 = leftPins[2]
        __initializeGPIO()

    def __initializeGPIO():
        # enA and enB are initialized by pi-blaster
        GPIO.setmode(GPIO.BCM) # Set GPIO numbers by BCM references
        # Right side wheels
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.output(self.in1, 0)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.output(self.in2, 0)
        # Left side wheels
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.output(self.in3, 0)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.output(self.in4, 0)

    def initializeGPIO():
        GPIO.setmode(GPIO.BCM) # Set GPIO numbers by BCM references
        # Right side wheels
        enA = 18
        in1 = 27
        GPIO.setup(in1, GPIO.OUT)
        GPIO.output(in1, 0)
        in2 = 22
        GPIO.setup(in2, GPIO.OUT)
        GPIO.output(in2, 0)
        # Left side wheels
        enB = 19
        in3 = 20
        GPIO.setup(in3, GPIO.OUT)
        GPIO.output(in3, 0)
        in4 = 21
        GPIO.setup(in4, GPIO.OUT)
        GPIO.output(in4, 0)


    
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


    def release():
        #GPIO.output(enA, 0)
        pwmRelease(enA)
        pwmRelease(enB)
        GPIO.output(in1, 0)
        GPIO.output(in2, 0)
        GPIO.output(in3, 0)
        GPIO.output(in4, 0)
        print('Cleanup!')
        GPIO.cleanup()

    def __setLeftWheelsForward():

    def __setRightWheelsForward():
        GPIO.output(self.in2, 0)
        GPIO.output(self.in1, 1)

    def __setRightWheelsBackwards():
        GPIO.output(self.in1, 0)
        GPIO.output(self.in2, 1)

    def __setLeftWheelsForward():
        GPIO.output(self.in4, 0)
        GPIO.output(self.in3, 1)

    def __setLeftWheelsBackwards():
        GPIO.output(self.in3, 0)
        GPIO.output(self.in4, 1)

    def accelerateForward(initV, endV, accelPeriod = 0.1, accelInc = 0.01):
        """
        Accelerates from initV with accelInc increments each accelPeriod time until it
        reaches the final endV
        :param initV initial dutycycle for pwm
        :param initV final dutycycle for pwm
        :param accelPeriod update interval in seconds
        :param accelInc dutycycle increase for each update interval
        """
    
    
if (__name__ == "__main__"):
    try:
        wheels = WheelsControl_L298N([18, 27, 22], [19, 21, 20]) # 21,20 instead of 20,21. Motors orientation is inverted on the left side

        wheels.release()


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
