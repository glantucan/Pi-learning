#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from leds.LED_RGB_PCA9685 import LED_RGB_PCA9685
from buttons.PushButton import PushButton
import RPi.GPIO as GPIO

if (__name__ == "__main__"):
    def onButtonPress(pin):
        print('Button ' +  buttons[pin]['colorName'] + ' pressed!')
        r =  buttons[pin]['color'][0]
        g =  buttons[pin]['color'][1]
        b =  buttons[pin]['color'][2]
        buttons[pin]['led'].setColor(r, g, b)
        buttons[pin]['button'].addEventCallback(GPIO.FALLING, onButtonRelease, 500)


    def onButtonRelease(pin):
        print('Button ' +  buttons[pin]['colorName'] + ' released!')
        buttons[pin]['led'].setColor(0, 0, 0)
        buttons[pin]['button'].addEventCallback(GPIO.RISING, onButtonPress, 500)

    buttons = {
        5: {
            'led': LED_RGB_PCA9685(1500, 14, 13, 12),
            'colorName': 'BLUE',
            'color': (0,0,1000),
            'button': PushButton(5)
        },
        6: {
            'led': LED_RGB_PCA9685(1500, 10, 9, 8),
            'colorName': 'RED',
            'color': (1000,0,0),
            'button': PushButton(6)
        },
        13: {
            'led': LED_RGB_PCA9685(1500, 6, 5, 4),
            'colorName': 'YELLOW',
            'color': (600, 400, 0),
            'button': PushButton(13)
        },
        19: {
            'led': LED_RGB_PCA9685(1500, 2, 1, 0),
            'colorName': 'GREEN',
            'color': (0, 1000, 0),
            'button': PushButton(19)
        }        
    }

    for pin in buttons:
        buttons[pin]['button'].addEventCallback(GPIO.RISING, onButtonPress, 500)

    try:
        print("Running")
        
        while(True):
            wait = True

    except KeyboardInterrupt:
        print("You pressed Ctrl+C. Exiting")
        GPIO.cleanup()