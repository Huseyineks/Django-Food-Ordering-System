from django.shortcuts import render,redirect
from .forms import OptionsForm
def OptionsFormView(request):
   form = OptionsForm(request.POST or None)
   context = dict(
      form = form
   )
   if form.is_valid():
      newForm = form.save()
      return redirect('homepage')
   return render(request,'form.html',context)
