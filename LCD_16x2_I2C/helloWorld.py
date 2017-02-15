
from Adafruit_CharLCD import Adafruit_CharLCD
import Adafruit_GPIO.PCF8574 as PCF
import time

GPIO = PCF.PCF8574(address=0x27)

# Define PCF pins connected to the LCD.
lcd_rs        = 4
lcd_en        = 6
d4,d5,d6,d7   = 0,1,2,3
cols,lines    = 16,2

# Instantiate LCD Display
lcd = Adafruit_CharLCD(lcd_rs, lcd_en, d4, d5, d6, d7,
                       cols, lines, gpio=GPIO)
lcd.clear()

lcd.message('  Raspberry Pi\n  I2C LCD 0x27')

time.sleep(5)
lcd.clear()
