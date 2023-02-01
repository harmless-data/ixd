from django.shortcuts import render
from django.conf import settings

import serial

# Create your views here.
def signalPLC(request,ean='no-override'):
    ser = serial.Serial(settings.ARDUINO_SERIAL,settings.ARDUINO_BAUD,timeout=1)
    ser.write(f'{ean % 9}'.encode())
    ser.close()
