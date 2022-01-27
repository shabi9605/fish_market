from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.contrib.auth.decorators import login_required


# Create your views here.

def product(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        products = products.filter(category=category)
    page = request.GET.get('page')
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)

    except PageNotAnInteger:
        products = paginator.page(1)

    except EmptyPage:
        products = paginator.page(1)
    is_authenticated = request.user.is_authenticated
    print(is_authenticated)
    if is_authenticated:
        # wishlist = Wishlist.objects.filter(user=request.user)

        return render(
            request,
            'product/shop.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
                # 'wishlist': wishlist
            }
        )

    else:
        return render(
            request,
            'product/shop.html',
            {
                'category': category,
                'categories': categories,
                'products': products,
            }
        )


def categorysearch(request,id):
    listing = get_object_or_404(Category, id=id)
    print(listing)
    product=Product.objects.order_by('-created').filter(category_id=listing.id)
    return render(request,'product/category.html',{'listings':product})


def product_search(request):
    results = None
    try:
        query = request.POST['query']
        results = Product.objects.filter(name__icontains=query) |\
            Product.objects.filter(description__icontains=query)
        page = request.GET.get('page')
        paginator = Paginator(results, 6)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(1)
        return render(
            request,
            'product/product.html',
            {'products': results}
        )
    except KeyError:
        wishlist = None
        "KeyError"
        return render(
            request,
            'product/product.html',
            {'products': results}
        )

def product_detail(request, id):
    products=Product.objects.all()
    product = get_object_or_404(
        Product,
        id=id,
        is_available=True
    )

    return render(
        request,
        'product/shop-detail.html',
        {'product': product,'list':products}
    )


# def category_create(request):
#     registerd=False
#     if request.method=='POST':
#         category_form=CategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             registerd=True
#         else:
#             HttpResponse('invalid form')
#     else:
#         category_form=CategoryForm()
#     return render(request,'product/create_category.html',{'registerd':registerd,'category_form':category_form})

def category_list(request):
    # user_instance=request.user.manager.branch_name
    list=Category.objects.all()
    return render(request,'product/category_view.html',{'list':list})



# def update_category(request,id):
#     Update = Category.objects.get(id=id)
#     print(Update)
#     form= CategoryForm(request.POST,instance=Update)
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Record Update succefully')
#         return render(request,'product/category_view.html',{'form':form,'category':Update})
#     return render(request,'product/category_edit.html',{'form':form,'category':Update})
    

# def delete_category(request,id):
#     deleteemp = Category.objects.get(id=id)
#     deleteemp.delete()
#     messages.success(request,'Record deleted succefully')
#     return render(request,'product/category_view.html')

# create Product
def product_create(request):
    if request.method=='POST':
        product_form=ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            P=Product(user=request.user,category=product_form.cleaned_data['category'],
            owner=request.user.market_owner,
            name=product_form.cleaned_data['name'],
            slug=product_form.cleaned_data['slug'],
            photo=product_form.cleaned_data['photo'],
            photo1=product_form.cleaned_data['photo1'],
            photo2=product_form.cleaned_data['photo2'],
            price=product_form.cleaned_data['price'],
            stock=product_form.cleaned_data['stock'],
            description=product_form.cleaned_data['description'],
            is_available=product_form.cleaned_data['is_available'],
            created=product_form.cleaned_data['created']
        
            )
            P.save()
            messages.success(request,'successfully added')
            return redirect('dashboard')
        else:
            HttpResponse('invalid form')
    else:
        product_form=ProductForm()
    return render(request,'product/create_product.html',{'product_form':product_form})

def product_list1(request):
    user_instance=request.user
    list=Product.objects.all().filter(user=user_instance)
    return render(request,'product/product_list.html',{'list':list})

# def edit_product(request,id):
#     editobj = Product.objects.get(id=id)
#     return render(request,'product/product_edit.html',{'product':editobj})

def update_product(request,id):
    Update = Product.objects.get(id=id)
    print(Update)
    form= ProductForm(instance=Update)
    if request.method=='POST':
        form= ProductForm(request.POST,request.FILES,instance=Update)
        if form.is_valid():
            form.save()
            messages.success(request,'Record Update succefully')
            return render(request,'product/product_list.html',{'form':form,'product':Update})
    return render(request,'product/product_edit.html',{'form':form,'product':Update})

def delete_product(request,id):
    deleteemp = Product.objects.get(id=id)
    deleteemp.delete()
    messages.success(request,'Record deleted succefully')
    return render(request,'product/product_list.html')

#product deatils





