#!/usr/bin/python
import lcddriver
import subprocess
import time

lcd = lcddriver.lcd()

def ScrollDisplay(curr):
  lcd.lcd_clear()
  # nasty hack to simulate scrolling text
  sep = " # "
  dispStr = curr + sep + curr + sep + curr + sep + curr + sep
  dispStr = dispStr + dispStr + dispStr
  strLen = len(dispStr)
  for i in range(0, strLen):
    lcd.lcd_clear()
    lcd.lcd_display_string(dispStr[i : i + 15], 1)
    lcd.lcd_display_string(dispStr[i + 16 : i + 31], 2)
    time.sleep(0.35)

while True:
  curr = subprocess.check_output(['mpc', 'current']).split('\n')
  print curr[0]
  ScrollDisplay(curr[0])
  time.sleep(10)
