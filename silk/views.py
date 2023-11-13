from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def silk(request):
    return HttpResponse('<center><h1>We are not taking about dairy milk silk</h1></center>')
