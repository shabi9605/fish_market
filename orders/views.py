from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from .models import *
from cart1.models import Cart
from account.models import Customer
from .forms import *
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.


def order_save(request):
    address=request.POST.get('address')
    address_second=request.POST.get('address_secound')
    postal_code = request.POST.get('zip')
    district = request.POST.get('district')
    city = request.POST.get('city')
    land_mark=request.POST.get('land')
   
    order = Order.objects.create(user=request.user,address=address,
    address_second=address_second,
    postal_code=postal_code,district=district,city=city,land_mark=land_mark
    
    )   
    cart = Cart.objects.get(user=request.user)
    order.save()
    request.session['order']=order.id
    for item in cart.items.all():
        orderItem, created = OrderItem.objects.update_or_create(user=order.user,
            order=order, product=item.product, price=item.price, quantity=item.quantity)
        order.order_items.add(orderItem)
        send_mail('Your Product is ordered','Plaese Contact with us ','shabi960580@gmail.com',[item.product.owner.user.email])
    return render(request,'payment/process.html')


def order_create(request):
    profile = get_object_or_404(Customer,user=request.user)
    cart = Cart.objects.get(user=request.user)
    return render(request, 'orders/order_list.html', {'cart': cart, 'profile': profile})

def orderview(request):
    order=OrderItem.objects.filter(seller=request.user.market_owner)
    print(order)
    print(request.user.id)
    return render(request,'order/order_view.html',{'order':order})

def orderitemview(request):
    order=OrderItem.objects.all()
    return render(request,'order/orderitem_view.html',{'order':order})

def neworder(request):
    a=OrderItem.objects.filter(user=request.user).order_by('-id')
    return render(request,'orders/neworder.html',{'order':a})

