from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Mukund Biradar Welcome to USA.")
def about(request):
    return HttpResponse("Shaurya Biradar Washington DC.")
def Contact(request):
    return HttpResponse("My Contact Number is :- 15646517211")