"""
URL configuration for project40 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('string_by_fbv/',string_by_fbv,name='string_by_fbv'),
    path('StringByCbv/',StringByCbv.as_view(),name='StringByCbv'),

    path('html_by_fbv/',html_by_fbv,name='html_by_fbv'),
    path('HtmlBYCbv/',HtmlBYCbv.as_view(),name='HtmlBYCbv'),


    path('insert_by_fbv/',insert_by_fbv,name='insert_by_fbv'),
    path('InsertByCbv/',InsertByCbv.as_view(),name='InsertByCbv'),


    path('HtmlByTV/',HtmlByTV.as_view(),name='HtmlByTV'),



    

]
