from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime



# Create your models here.

Thiruvananthapuram = 'Thiruvananthapuram'
Kollam = 'Kollam'
Alappuzha= 'Alappuzha'
Pathanamthitta = 'Pathanamthitta'
Kottayam = 'Kottayam'
Idukki = 'Idukki'
Ernakulam = ' Ernakulam'
Thrissur= 'Thrissur'
Palakkad = 'Palakkad'
Malappuram = 'Malappuram'
Kozhikode = ' Kozhikode'
Wayanadu= 'Wayanadu'
Kannur = 'Kannur'
Kasaragod = 'Kasaragod'

District_name =(
    (Thiruvananthapuram , 'Thiruvananthapuram'),
    (Kollam , 'Kollam'),
    (Alappuzha , 'Alappuzha'),
    (Pathanamthitta , 'Pathanamthitta'),
    (Kottayam , 'Kottayam'),
    (Idukki , 'Idukki'),
    ( Ernakulam , ' Ernakulam'),
    (Thrissur, 'Thrissur'),
    (Palakkad , 'Palakkad'),
    (Malappuram , 'Malappuram'),
    (Kozhikode, ' Kozhikode'),
    (Wayanadu, 'Wayanadu'),
    (Kannur , 'Kannur'),
    (Kasaragod , 'Kasaragod')
)

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField(blank=True)
    image=models.ImageField(upload_to='images',default='default.jpg')
    house_name=models.CharField(max_length=50,blank=True,null=True)
    district=models.CharField(max_length=30,choices=District_name,default=Thrissur)
    city=models.CharField(max_length=30,blank=True,null=True)
    pincode=models.PositiveIntegerField(blank=True,null=True)
    land_mark=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return str(self.user.username)

class Market_owner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber=PhoneNumberField()
    photo=models.ImageField(upload_to='manager_photos/%Y/%m/%d/')
    market_name=models.CharField(max_length=50,blank=True,null=True)
    district=models.CharField(max_length=30,choices=District_name,default=Thrissur)
    city=models.CharField(max_length=30,blank=True,null=True)
    pincode=models.PositiveIntegerField(blank=True,null=True)
    land_mark=models.CharField(max_length=100,blank=True,null=True)
    licence_number=models.CharField(max_length=150)
    proof=models.FileField(upload_to='owner_proof')
    market_image=models.ImageField(upload_to='market_image',default="default.jpg")
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
         return str(self.user.username)




class Market(models.Model):
    market_name=models.CharField(max_length=50)
    market_place=models.CharField(max_length=50)
    district=models.CharField(max_length=30,choices=District_name,default=Thrissur)
    city=models.CharField(max_length=30,blank=True,null=True)
    pincode=models.PositiveIntegerField(blank=True,null=True)
    land_mark=models.CharField(max_length=100,blank=True,null=True)
    market_image=models.ImageField(upload_to='market_image',default="default.jpg")
    def __str__(self):
         return str(self.market_name)

