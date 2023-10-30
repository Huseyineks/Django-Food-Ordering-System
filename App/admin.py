from django.contrib import admin

from .models import Options,Paying,Item

@admin.register(Item)
class AppAdmin(admin.ModelAdmin):
    class Meta:
     model = Item
@admin.register(Options)
class AppAdmin(admin.ModelAdmin):
    list_display = ['size','temp']
    list_display_links = ['size','temp']
    class Meta:
        
       
        model = Options
@admin.register(Paying)     
class AppAdmin(admin.ModelAdmin):
    
    class Meta:
        
       
        model = Paying
        



