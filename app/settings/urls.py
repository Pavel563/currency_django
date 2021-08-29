import accounts
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from currency.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
