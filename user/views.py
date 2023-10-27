from django.shortcuts import render,redirect
from .forms import OptionsForm
from django.views.generic import View




class OptionsFormView(View):
    def get(self,request,*args,**kwargs):
      return render(request,'form.html')
    


    def post(self,request,*args,**kwargs):
      form = OptionsForm(request.POST)
      if form.is_valid():
         newUser = form.save()
         return redirect('homepage')
      return render(request,'form.html',{'form':form})

# def OptionsFormView(request):
#    form = OptionsForm(request.POST or None)
#    context = dict(
#       form = form
#    )
#    if form.is_valid():
#       newForm = form.save()
#       return redirect('homepage')
#    return render(request,'form.html',context)

