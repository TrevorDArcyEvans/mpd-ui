#!/usr/bin/env python

import os
from time import sleep

import RPi.GPIO as GPIO

# input buttons
MpcPrev = 14
MpcToggle = 15
MpcNext = 16
MpcReady = 17

# disable warnings
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(MpcPrev, GPIO.IN)
GPIO.setup(MpcToggle, GPIO.IN)
GPIO.setup(MpcNext, GPIO.IN)

# turn on ready LED
GPIO.setup(MpcReady, GPIO.OUT)
sleep(1);
GPIO.output(MpcReady, True)

while True:
    if (GPIO.input(MpcPrev) == True):
        os.system('mpc prev &')

    if (GPIO.input(MpcToggle) == True):
        os.system('mpc toggle &')

    if (GPIO.input(MpcNext)== True):
        os.system('mpc next &')

    sleep(0.1);

