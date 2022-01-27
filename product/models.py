from django.db import models
from datetime import datetime
from account.models import Market_owner,Customer
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,db_index=True)
    description=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image=models.ImageField(upload_to='category_image')
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])

   
class Product(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    owner=models.ForeignKey(Market_owner,on_delete=models.CASCADE,blank=True,null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    photo=models.ImageField(upload_to='product_image/%Y/%m/%d')
    photo1=models.ImageField(upload_to='product_image/%Y/%m/%d',blank=True,null=True)
    photo2=models.ImageField(upload_to='product_image/%Y/%m/%d',blank=True,null=True)
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('account:product_detail', args=[self.id, self.slug])


    