from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','phone','image',]
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Market_owner)
admin.site.register(Market)
    