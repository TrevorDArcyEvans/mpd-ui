#!/usr/bin/python
import lcddriver
import subprocess
import time

lcd = lcddriver.lcd()

def current():
  return subprocess.check_output(['mpc', 'current']).split('\n')[0]

def ScrollDisplay(curr):
  lcd.lcd_clear()
  # nasty hack to simulate scrolling text
  sep = " # "
  dispStr = curr + sep + curr + sep
  strLen = len(dispStr)
  for i in range(0, strLen):
    lcd.lcd_clear()
    lcd.lcd_display_string(dispStr[i : i + 15], 1)
    lcd.lcd_display_string(dispStr[i + 16 : i + 31], 2)
    time.sleep(0.40)
    if i%10 == 0:
      msg = current()
      if msg != curr:
        return

while True:
  curr = current()
  #print curr
  ScrollDisplay(curr)
