"""m4market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('registers',views.registers,name='registers'),
    path('registerdone',views.registerdone,name='registerdone'),
    path('login',views.login,name='login'),
    path('logindone',views.logindone,name='logindone'),
    path('searchcategory',views.searchcategory,name='searchcategory'),
    path('searchitem',views.searchitem,name='searchitem'),
    path('addtobusket',views.addtobusket,name='addtobusket'),
    path('viewbusket',views.viewbusket,name='viewbusket'),
    path('deletecart',views.deletecart,name='deletecart'),
    path('buy1',views.buy1,name='buy1'),
    path('myorder',views.myorder,name='myorder'),
    path('logout',views.logout,name='logout'),
    path('update',views.update,name='update'),
    path('orders',views.orders,name='orders'),
    path('updateit',views.updateit,name='updateit'),
    path('searchcategoryadmin',views.searchcategoryadmin,name='searchcategoryadmin'),
    path('searchitemadmin',views.searchitemadmin,name='searchitemadmin'),
    path('ordershow',views.ordershow,name='ordershow'),
    path('ordersend',views.ordersend,name='ordersend'),
    path('orderreceive',views.orderreceive,name='orderreceive'),
    path('orderidset',views.orderidset,name='orderidset'),
    path('userlistview',views.userlistview,name='userlistview'),
    path('adminhome',views.adminhome,name='adminhome'),
]
