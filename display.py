#!/usr/bin/python

import RPi.GPIO as GPIO
import smbus
import time


i2c = smbus.SMBus(1)  # Use 0 for older RasPi

GPIO.setmode(GPIO.BCM)  # Board numbering
GPIO.setup(23, GPIO.OUT)
GPIO.setup(0, GPIO.OUT)  # SDA

address = 0x3a  # Address of LCD-Modul TIAN MA A2C00096100 (probably) or (0x76)
TCA9548A = 0x70


def channel(address=0x74, channel=0):  # Switcher

    if channel == 0:
        action = 0x04
    elif channel == 1:
        action = 0x05
    elif channel == 2:
        action = 0x06
    elif channel == 3:
        action = 0x07
    else:
        action = 0x00

    i2c.write_byte_data(address, 0x04, action)  # 0x04 is the register for switching channels


# Our I2C code
# First setup
i2c.write_i2c_block_data(address, 0x00, [0x20, 0x06, 0x0E, 0x21, 0x04, 0x42, 0x08, 0xB0, 0xC0, 0x20])
# Trying to write AAAAAAAAAA
i2c.write_i2c_block_data(address, 0x00, [0x40, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41, 0x41])