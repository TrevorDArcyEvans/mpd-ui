#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)

while True:
    if (GPIO.input(14) == True):
        os.system('mpc prev &')

    if (GPIO.input(15) == True):
        os.system('mpc toggle &')

    if (GPIO.input(16)== True):
        os.system('mpc next &')

    sleep(0.1);

