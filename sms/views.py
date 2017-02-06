from django.shortcuts import render
from django.http import HttpResponse
from sms import smslib


def handlePost(request, phone, message):
    sendResult = smslib.sendSms (phone, message)
    print ("Result of SMS lkib call: {0}".format (sendResult))
    return HttpResponse("Your message '{0}' has been sent to {1}".format (message, phone))
