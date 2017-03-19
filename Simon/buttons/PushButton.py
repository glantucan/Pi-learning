#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

class PushButton(object):
    """Creates a push button object able to detect RISING or FALLING events and call 
    calback functions in response to them
    Upon creation if a callback is specified an event is registered for GPIO.RISING.
    """
    # TODO: Try Detecting release before detecting press again to avoid bouncing.
    # Could also be because the bad quality of the buttons
    
    def __init__(self, pin, pressCallback = None, bounceTime = 400):
        self.__pin = pin
        self.__edgeMode = None
        self.__FALLING_events_active = False        
        self.__isActive = True
        self.__hasCallbacks = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
        if (pressCallback):
            self.hasCallbacks = True
            self.__edgeMode = GPIO.RISING
            GPIO.add_event_detect(pin, GPIO.RISING, callback = pressCallback, bouncetime = bounceTime)

    def enable(self):
        if not self.__isActive:
            GPIO.setup(self.__pin, GPIO.IN)
            self.__isActive == True
            
    def disable(self):
        if self.__isActive:
            GPIO.setup(self.__pin, GPIO.OUT)
            GPIO.output(self.__pin, GPIO.LOW)
            self.__isActive = False

    def destroy(self):
        '''Properly destroys the object cleaning up events and reseting the pin to br
        and output pin with its value set to LOW
        '''
        self.disable()
        self.__pin = None
        self.removeEventCallbacks()
    
    def getValue(self):
        '''Gets the input value of the pin associated with the button. 
        Useful in a polling loop
        '''
        return GPIO.input(self.__pin)

    def waitTillPress(self, timeout = 5000):
        '''Waits until the button is pressed. The program is paused. '''
        wait_for_edge(self.__pin, GPIO.RISING, timeout = timeout)
    
    def waitTillRelease(self, timeout = 5000):
        '''Waits until the button is released. The program is paused. '''
        wait_for_edge(self.__pin, GPIO.FALLING, timeout = timeout)
    
    def removeEvent(self):
        GPIO.remove_event_detect(self.__pin)
        self.__edgeMode = None


    def addEventCallback(self, edgeMode, callback, bounceTime = 200):
        '''Adds an event callback to the GPIO.RISING or GPIO.FALLING end as specified.
        Only one callback is supported so previous ones will be forgotten.
        '''
        # There seems to be a bug in RPi.GPIO, adding more than one callback makes all
        # of them to be called more than once when the event triggers.
        # Not a very big deal since the only parametter passed is the pin number, 
        # so having a central callback in an object with the needed state accesible 
        # is needed anyway.
        # Consider implementing observer pattern from this class if more than one 
        # callback is desirable
        if self.__edgeMode != None:
            self.removeEvent()

        GPIO.add_event_detect(self.__pin, edgeMode, callback = callback, bouncetime = bounceTime)
        self.__edgeMode = edgeMode



    @property
    def isEnabled(self):
        return self.__isActive


if (__name__ == "__main__"):
    def onButtonPress(pin):
        print('Button pressed!')

    def onButtonPress2(pin):
        print('Button pressed 2nd callback!')

    def onButtonPress3(pin):
        print('Button pressed 3rd callback!')

    def onButtonPress4(pin):
        print('Button pressed 4rth callback!')

    try:
        print("something")
        button1 = PushButton(5)
        button1.addEventCallback(GPIO.RISING, onButtonPress, 500)
        button2 = PushButton(6)
        button2.addEventCallback(GPIO.RISING, onButtonPress2, 500)
        button3 = PushButton(13)
        button3.addEventCallback(GPIO.RISING, onButtonPress3, 500)
        button4 = PushButton(19)
        button4.addEventCallback(GPIO.RISING, onButtonPress4, 500)



        
        while(True):
            wait = True

    except KeyboardInterrupt:
        print("You pressed Ctrl+C. Exiting")
        GPIO.cleanup()