from django.contrib import admin
from .models import OrderedItem
@admin.register(OrderedItem)
class AppAdmin(admin.ModelAdmin):
    class Meta:
     model = OrderedItem
