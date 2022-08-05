"""site1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views # this import all methods in the views.py of app1

# import django.urls import path,re_path

from django.urls import path, re_path, include
# from . import views
# from app1.views import index
# from app1.views import add // this import specific method
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('login/',views.login,name='login'),
    path('logout/',views.logout , name='logout'),
    path('home/',views.home),
    path('adminu/',views.moves),
    path('jewelsa/',views.jeweladd),
    path('jewels/',views.jewels),
    path('admincontrol/',views.admincontrol),
    path('profile/',views.profile,name='profile'),
    path('update/',views.update),
    path('jewelsd/',views.delete),
    path('index/',views.index),
    # path('cart/',views.cart,name="cart"),
    path('datacart/',views.datacart),
    path('contact/',views.contact),
    path('product/',views.product),
    path('updateCart/',views.updateCart),
    path('deleteCart/',views.deleteCart),
    # path('pay/',views.payment),
    path('cart/',views.HomePageView.as_view(), name='cart'),
    path('charge/',views.charge, name='charge'),
    path('collections/',views.collections),
    path('about/',views.about),
    path('adminUsers/',views.adminUsers),
    path('deleteJewels/',views.deleteJewels),
    path('adminDelete/',views.adminDelete),
    path('orderHistory/',views.orderHistory, name='orderHistory'),
    path('allOrders/',views.allOrders, name='allOrders'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)