from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

command = "<title>To-Do lists</title><body>hello world</body>"

def home_page(request):
    return HttpResponse(command)
