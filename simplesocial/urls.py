"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.HomePage.as_view(),name="home"),
    path('munnar/',views.MunnarPage.as_view(),name="munnar"),
    path('alappuzha/',views.AlappuzhaPage.as_view(),name="alappuzha"),
    path('kottayam/',views.KottayamPage.as_view(),name="kottayam"),
    path('kannur/',views.KannurPage.as_view(),name="kannur"),
    path('wayanad/',views.WayanadPage.as_view(),name="wayanad"),
    path('thrissur/',views.ThrissurPage.as_view(),name="thrissur"),
    path('connect/',views.ConnectPage.as_view(),name="connect"),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('test/',views.TestPage.as_view(),name="test"),
    path('thanks',views.ThanksPage.as_view(),name="thanks"),
    path('posts/',include('posts.urls')),
    path('groups/',include('groups.urls'))

]
