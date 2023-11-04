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
      size = request.POST.get('size')
      temp = request.POST.get('temp')
      if (size is None) or (temp is None):
        context = dict(
          error = 'Fill in the blanks!'
        )
        return render(request,'form.html',context)
      elif form.is_valid():
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
      payoptions = request.POST.get('payoptions')
      if payoptions is None:
        context = dict(
          error = 'Fill in the blanks!'
        )
        return render(request,'paying.html',context)
      elif form.is_valid():
         payingmethod = form.save(commit=False)
         payingmethod.id = request.POST.get('ids')
         payingmethod.save()
         item = Item.objects.get(id = request.POST.get('ids'))
         options = Options.objects.get(id = request.POST.get('ids'))
         paying = Paying.objects.get(id = request.POST.get('ids'))
         ordereditem = OrderedItem.objects.create(user = request.user,name = item.name,price = item.price,size = options.size,temp = options.temp,request = options.request,payoptions = paying.payoptions)
         
        
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
      get_User = User.objects.get(username = request.user)
      context = dict(
        form = get_User
      )
      return render(request,'information.html',context)
    


   def post(self,request,*args,**kwargs):
      
      username = request.POST.get('username')
      password = request.POST.get('password')
      confirmpassword = request.POST.get('confirm-password')
      email = request.POST.get('email')
      if password != confirmpassword:
        return render(request,'information.html',{'error':True})
      elif not password and not confirmpassword and not username and not email:
        return render(request,'information.html',{'error2':True})
      else:
         get_User = User.objects.get(username = request.user)
        
         if (get_User.username != username) and (username is not None):
           get_User.username = username
         else:
           get_User.username = get_User.username
         if (get_User.password != password) and (password is not None):
           get_User.password = password
         else:
           get_User.password = get_User.password
         if (get_User.email != email) and (email is not None):
           get_User.email = email
         else:
           get_User.email = get_User.email
                
        
             
         get_User.save()
         login(request,get_User)
         return redirect('homepage')
      


def basket(request):
  orders = OrderedItem.objects.filter(user = request.user)
  context = dict(
    orders = orders
  )
  return render(request,'basket.html',context)    


