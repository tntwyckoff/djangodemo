from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from hexlib import hexlib

def parseDefaultToken(request):
    inputString = '87ae'
    hexString = hexlib.convertHexStringToDecimal (inputString)
    return HttpResponse("Hex-decoded value for string '{0}': {1}".format (inputString, hexString))