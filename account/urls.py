from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name="index"),
    path('register/',views.register,name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('password/',views.change_password,name="change_password"),
    path('update_profile_customer/',views.update_profile_customer,name='update_profile_customer'),
    path('update_profile_owner/',views.update_profile_owner,name='update_profile_owner'),

    path('register_owner',views.register_owner,name='register_owner'),
    path('search_product',views.search_product,name='search_product'),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)