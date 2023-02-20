from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def monis(request):
    return HttpResponse("hello aiman.tommorrow you are going to school or not")