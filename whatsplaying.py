#!/usr/bin/python
import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_display_string("I love Mandy", 1)
lcd.lcd_display_string("I love Ellie", 2)

