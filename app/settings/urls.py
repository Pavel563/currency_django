"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from currency.views import hello, generate_password, rate_list, rate_details, source_list, source_details, table_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('gen-pas/', generate_password),
    path('currency/rate/list/', rate_list),
    path('currency/rate/details/<int:pk>/', rate_details),
    path('currency/source/list/', source_list),
    path('currency/source/details/<int:pk>/', source_details),
    path('table/', table_test)
]
