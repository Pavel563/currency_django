from django.urls import path
from accounts import views



app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('singup/', views.SingUp.as_view(), name='singup'),
    path('activate/account/<uuid:activation_key>', views.ActivateAccount.as_view(), name='activate-account'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.ActivateAccount.activate, name='activate'),

]