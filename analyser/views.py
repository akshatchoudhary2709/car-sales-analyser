#created by user
from django.http import HttpResponse
from django.shortcuts import render
import pickle

def index(request):
    return render(request, 'index.html')

#def main(request):


def audi(request):
    return render(request,'audi.html')

def volkswagen(request):
    return render(request,'volkswagon.html')

def porsche(request):
    return render(request,'porsche.html')

def mercedes(request):
    return render(request,'mercedes.html')

def bugatti(request):
    return render(request,'bugatti.html')


