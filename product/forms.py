from django import forms
from django.db.models import fields
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = ('name','description')


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ('category','name','slug','photo','photo1','photo2','price','stock','description',
        'is_available','created')