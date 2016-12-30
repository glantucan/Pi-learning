#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

import time

letterMap = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
		'Ñ': '--.--',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

dashTime = 0.27
dotTime = 0.09

LedPin = 11 # physical number correponding to GPIO0 (GPIO17)

GPIO.setmode(GPIO.BOARD) # Set GPIO numbers by physical location
GPIO.setup(LedPin, GPIO.OUT) # Set LedPin's mode as output
GPIO.output(LedPin, GPIO.HIGH) # Set LedPin as high (3.3V) to turn off the led


def dot():
	GPIO.output(LedPin, GPIO.LOW)
	time.sleep(dotTime)
	GPIO.output(LedPin, GPIO.HIGH)
	time.sleep(dotTime)

def dash():
	GPIO.output(LedPin, GPIO.LOW)
	time.sleep(dashTime)
	GPIO.output(LedPin, GPIO.HIGH)
	time.sleep(dotTime)

message = "Hola mundo."
	
try:
	for letter in message:
		if letter != ' ':
			curLetterCode = letter + ': '
			for signal in letterMap[letter.upper()]:
				if signal == '-':
					dash()
					curLetterCode += '-'
				elif signal == '.':
					dot()
					curLetterCode += '.'
					
		else:
			#GPIO.output(LedPin, GPIO.HIGH)
			time.sleep(dashTime)
			print('word separator')
		print(curLetterCode)
	

	GPIO.output(LedPin, GPIO.HIGH)
	GPIO.cleanup()
	print('message finished')
	
except KeyboardInterrupt:
	GPIO.output(LedPin, GPIO.HIGH)
	GPIO.cleanup()
