from django.shortcuts import render,redirect
from .forms import OptionsForm,PayingForm
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms
from App.models import Item,Paying,Options
from .models import OrderedItem




class OptionsFormView(View):
    def get(self,request,*args,**kwargs):
      return render(request,'form.html')
    


    def post(self,request,*args,**kwargs):
      form = OptionsForm(request.POST)
      if form.is_valid():
         newOption = form.save(commit=False)
         newOption.id = request.POST.get('ids')
         newOption.save() 
         
         
         context = dict(
           id = request.POST.get('ids')
         )
         return render(request,'paying.html',context)
         
         
      return render(request,'form.html',{'form':form})
    
class PayingFormView(View):
    def get(self,request,*args,**kwargs):
      return render(request,'paying.html')
    


    def post(self,request,*args,**kwargs):
      form = PayingForm(request.POST)
      if form.is_valid():
         payingmethod = form.save(commit=False)
         payingmethod.id = request.POST.get('ids')
         payingmethod.save()
         item = Item.objects.get(id = request.POST.get('ids'))
         options = Options.objects.get(id = request.POST.get('ids'))
         paying = Paying.objects.get(id = request.POST.get('ids'))
         ordereditem = OrderedItem.objects.create(name = item.name,price = item.price,size = options.size,temp = options.temp,request = options.request,payoptions = paying.payoptions)
        
        
         return redirect('homepage')
      return render(request,'paying.html',{'form':form})
    

class LoginFormView(View):
    def get(self,request,*args,**kwargs):
      return render(request,'login.html')
    


    def post(self,request,*args,**kwargs):
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(username = username,password = password)
      if user is not None:
        login(request,user)
        return redirect('homepage')
      else:
        context = {
           'error':'There is no such an account.'
        }
        return render(request,'login.html',context)
            

class RegisterFormView(View):
    

    def get(self,request,*args,**kwargs):
      return render(request,'register.html')
    


    def post(self,request,*args,**kwargs):
      username = request.POST.get('username')
      password = request.POST.get('password')
      confirmpassword = request.POST.get('confirm-password')
      email = request.POST.get('email')
      if password != confirmpassword:
        return render(request,'register.html',{'error':True})
      elif not password and not confirmpassword and not username and not email:
        return render(request,'register.html',{'error2':True})
      else:
         newUser = User.objects.create_user(username=username,email=email,password=password)
         newUser.save()
         login(request,newUser)
         return redirect('homepage')
def logOut(request):
  logout(request)
  return redirect('homepage')         
      
def order(request,id):
  item = Item.objects.get(id = id)
  if request.POST.get('control') == 'clicked':
     
   context = dict(
     id = item.id
     
   )
   return render(request,'form.html',context)
  
  context = dict(
     item = item
  )
  return render(request,'order.html',context)
  
class InformationUpdateFormView(View):
    

    def get(self,request,*args,**kwargs):
      return render(request,'register.html')
    


    def post(self,request,*args,**kwargs):
      username = request.POST.get('username')
      password = request.POST.get('password')
      confirmpassword = request.POST.get('confirm-password')
      email = request.POST.get('email')
      if password != confirmpassword:
        return render(request,'register.html',{'error':True})
      elif not password and not confirmpassword and not username and not email:
        return render(request,'register.html',{'error2':True})
      else:
         newUser = User.objects.create_user(username=username,email=email,password=password)
         newUser.save()
         login(request,newUser)
         return redirect('homepage')


