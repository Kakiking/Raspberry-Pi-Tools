#!/usr/bin/python

import RPi.GPIO as GPIO

class PfeiltastenHandler(parent=None):
    def __init__(UP_pin=37, DOWN_pin=33, LEFT_pin=22, RIGHT_pin=35):
        self.ButtonUP_pin = UP_pin
        self.ButtonDOWN_pin = DOWN_pin
        self.ButtonLEFT_pin = LEFT_pin
        self.ButtonRIGHT_pin = RIGHT_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ButtonUP_pin, GPIO.IN)
        GPIO.setup(ButtonDOWN_pin, GPIO.IN)
        GPIO.setup(ButtonLEFT_pin, GPIO.IN)
        GPIO.setup(ButtonRIGHT_pin, GPIO.IN)
    def check_for_input():
        if (GPIO.input(self.ButtonUP_pin) == 0):
            return "up"
        if (GPIO.input(self.ButtonDOWN_pin) == 0):
            return "down"
        if (GPIO.input(self.ButtonLEFT_pin) == 0):
            return "left"
        if (GPIO.input(self.ButtonRIGHT_pin) == 0):
            return "right"
    finally:
        GPIO.cleanup()

