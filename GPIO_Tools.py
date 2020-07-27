#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class PfeiltastenHandler(parent=None):
    def __init__(self, UP_pin=37, DOWN_pin=33, LEFT_pin=22, RIGHT_pin=35):
        self.ButtonUP_pin = UP_pin
        self.ButtonDOWN_pin = DOWN_pin
        self.ButtonLEFT_pin = LEFT_pin
        self.ButtonRIGHT_pin = RIGHT_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ButtonUP_pin, GPIO.IN)
        GPIO.setup(self.ButtonDOWN_pin, GPIO.IN)
        GPIO.setup(self.ButtonLEFT_pin, GPIO.IN)
        GPIO.setup(self.ButtonRIGHT_pin, GPIO.IN)
    def check_for_input(self):
        if (GPIO.input(self.ButtonUP_pin) == 0):
            return "up"
        if (GPIO.input(self.ButtonDOWN_pin) == 0):
            return "down"
        if (GPIO.input(self.ButtonLEFT_pin) == 0):
            return "left"
        if (GPIO.input(self.ButtonRIGHT_pin) == 0):
            return "right"

class Ultraschallsensor():
    def __init__(self, trig=36, echo=32):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.TRIG = trig
        self.ECHO = echo
        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)
    def get_distance(self):
        print("Getting distance")
        GPIO.output(self.TRIG, False)
        time.sleep(2)
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)
        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        return pulse_duration
    def transform_to_cm(self, pulse_duration, i):
        distance = pulse_duration * 17150
        distance = round(distance, i)
        return "Distance: " + str(distance) + "cm"
