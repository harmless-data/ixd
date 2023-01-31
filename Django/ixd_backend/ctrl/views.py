from django.shortcuts import render
from django.conf import settings

import serial

# Create your views here.
def signalPLC(request):
    ser = serial.Serial(settings.ARDUINO_SERIAL,settings.ARDUINO_BAUD,timeout=1)
    ser.write(b'test')
    ser.close()
