from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(OrderItem)
class Adminorder(admin.ModelAdmin):
    list_display=['address','postal_code','district','city','land_mark','created','updated']
    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self,request,obj=None):
        return False
    def has_update_permission(self,request,obj=None):
        return False
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(Adminorder, self).changeform_view(request, object_id, extra_context=extra_context)

admin.site.register(Order,Adminorder)