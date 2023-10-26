from django.contrib import admin

from .models import Options
class AppAdmin(admin.ModelAdmin):
    class Meta:
        model = Options
        fields = '__all__'




admin.site.register(Options,AppAdmin)