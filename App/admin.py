from django.contrib import admin

from .models import Options,Paying
class AppAdmin(admin.ModelAdmin):
    
    class Meta:
        
       
        model = Options
        fields = '__all__'
class AppAdmin(admin.ModelAdmin):
    
    class Meta:
        
       
        model = Paying
        fields = '__all__'




admin.site.register(Options,AppAdmin)
admin.site.register(Paying,AppAdmin)