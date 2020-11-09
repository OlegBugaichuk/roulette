from django.shortcuts import render
from django.http import Http404
from .models import Item

# Create your views here.

def index_view(request):
    if request.method == 'GET':
        items = Item.objects.filter(visible=True)
        return render(request, 'core/index.html', {'items': items})
    else:
        raise Http404()