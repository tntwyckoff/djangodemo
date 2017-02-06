from django.shortcuts import render
from django.http import HttpResponse
from samples import sampleLib


def bmi_imperial(request, weight, height):
    return HttpResponse("Calculated BMI (Imperial): {0}".format (sampleLib.imperial_bmi (weight, height)))

def bmi_metric(request, weight, height):
    return HttpResponse("Calculated BMI (Metric): {0}".format (sampleLib.metric_bmi (weight, height)))