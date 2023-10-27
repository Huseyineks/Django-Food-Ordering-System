from django.contrib import admin
from django.urls import path,include
from user import views
app_name = 'user'
urlpatterns = [
   
    path('form/', views.OptionsFormView.as_view(),name='form'),
    

]