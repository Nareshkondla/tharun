from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def naresh(request):
    return HttpResponse("<h1>Hello tussu, Come To Game.</h1>")