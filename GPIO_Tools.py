#!/usr/bin/python

import RPi.GPIO as GPIO

class PfeiltastenHandler():
    def __init__(parent=None):
        ButtonUP_pin = 37
        ButtonDOWN_pin = 33
        ButtonLEFT_pin = 22
        ButtonRIGHT_pin = 35

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ButtonUP_pin, GPIO.IN)
        GPIO.setup(ButtonDOWN_pin, GPIO.IN)
        GPIO.setup(ButtonLEFT_pin, GPIO.IN)
        GPIO.setup(ButtonRIGHT_pin, GPIO.IN)
    def check_for_input():
        if (GPIO.input(ButtonUP_pin) == 0):
            return "up"
        if (GPIO.input(ButtonDOWN_pin) == 0):
            return "down"
        if (GPIO.input(ButtonLEFT_pin) == 0):
            return "left"
        if (GPIO.input(ButtonRIGHT_pin) == 0):
            return "right"
    finally:
        GPIO.cleanup()

