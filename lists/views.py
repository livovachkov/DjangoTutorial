from django.shortcuts import render
from django.http import HttpResponse


#from lists.globals import command //the file was removed in change of refractoring

# Create your views here.

#command = "<html><title>To-Do lists</title><body>hello world</body></html>"

def home_page(request):
    #return HttpResponse(command) #goes with command from lists.globals
    return render(request, 'home.html')
