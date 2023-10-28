from django.contrib import admin
from django.urls import path,include
from user import views
app_name = 'user'
urlpatterns = [
   
    path('form/', views.OptionsFormView.as_view(),name='form'),
    path('register/', views.RegisterFormView.as_view(),name='register'),
    path('login/', views.LoginFormView.as_view(),name='login'),
    path('logout/', views.logOut,name='logout'),
    

]