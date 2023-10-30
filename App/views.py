from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
    ıtems = Item.objects.all()
    context = dict(
        ıtems = ıtems
    )
    return render(request,'homepage.html',context)