from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item, List

#from lists.globals import command //the file was removed in change of refractoring

# Create your views here.

#command = "<html><title>To-Do lists</title><body>hello world</body></html>"
'''
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')



    #return HttpResponse(command) #goes with command from lists.globals
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
'''
def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')