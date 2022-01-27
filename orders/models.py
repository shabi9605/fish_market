from django.db import models
from product.models import Product
from account.models import *


pending='pending'
packed='packed'
shipped='shipped'
delivered='delivered'
delivery_statuses=[
        (pending,'pending'),
        (packed,'packed'),
        (shipped,'shipped'),
        (delivered,'delivered')
    ]
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    address = models.CharField(max_length=250)
    address_second = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=20)
    district = models.CharField(max_length=100) 
    city = models.CharField(max_length=100)
    land_mark=models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=delivery_statuses,default=pending)
    deliverd_date=models.DateField(default=timezone.now)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {} {}'.format(self.user, self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.order_items.all())


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    order = models.ForeignKey(Order,
    related_name='order_items',
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='order_products',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    seller=models.ForeignKey(Market_owner,on_delete=models.CASCADE,blank=True,null=True)


    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def save(self,*args,**kwargs):
        s=OrderItem.objects.prefetch_related('product').all() 
        print(s)
        self.seller=self.product.user.market_owner
        print(self.seller)
        super().save(*args, **kwargs)