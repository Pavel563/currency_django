import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from currency.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('currency/', include('currency.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
