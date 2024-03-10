from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('HELLO WELLCOME TO BLOOD')

def introduce(request):
    return HttpResponse('CAN YOU PREPARE TO HAVE A GOOD JOB')