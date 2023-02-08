from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest

import serial

# Create your views here.
def signalPLC(request,signal='no-override'):
    '''signalPLC singals attached arduino PLC

    Args:
        request (http request): Http Request Object
        signal (str, optional): singal to be sent to PLC. Defaults to 'no-override'.

    Returns:
        HttpResponse: 200 Response
    '''
    if signal == 'no-override':
        return HttpResponseBadRequest('no signal delivered')

    ser = serial.Serial(settings.ARDUINO_SERIAL,settings.ARDUINO_BAUD,timeout=1)
    _singal = int(signal) % 100
    ser.write(f'{_singal}'.encode())
    ser.close()
    return HttpResponse('')
