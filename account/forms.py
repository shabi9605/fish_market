
from django import forms
from django.forms.widgets import PasswordInput, Widget
from .models import *
from django.forms import ModelForm, fields

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=('username','email','password1','password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('phone','image')

class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('phone','image','house_name','district','city','pincode','land_mark')



class MarketOwnerForm(forms.ModelForm):
    hire_date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Market_owner
        fields=('phonenumber','photo','market_name','district','city','pincode','land_mark','licence_number','proof','market_image','hire_date')

class UpdateMarketForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    class Meta:
        model=User
        fields=('username','email','first_name','last_name')

class UpdateProfileMarketForm(forms.ModelForm):
    class Meta:
        model=Market_owner
        fields=('phonenumber','photo','market_name','district','city','pincode','land_mark','market_image')


