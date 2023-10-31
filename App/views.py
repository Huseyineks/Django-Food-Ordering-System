from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    items = Item.objects.all()
    context = dict(
        items = items
    )
    return render(request,'homepage.html',context)