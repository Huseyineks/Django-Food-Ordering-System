from django.contrib import admin
from django.urls import path,include
from user import views
app_name = 'user'
urlpatterns = [
   
    path('options/', views.OptionsFormView.as_view(),name='options'),
    path('paying/', views.PayingFormView.as_view(),name='paying'),
    path('register/', views.RegisterFormView.as_view(),name='register'),
    path('login/', views.LoginFormView.as_view(),name='login'),
    path('logout/', views.logOut,name='logout'),
    path('order/<int:id>', views.order,name='order'),
    

]