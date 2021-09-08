from django.urls import path
from accounts import views



app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('signup/', views.SingUp.as_view(), name='signup'),
    path('activate/account/<uuid:activation_key>', views.ActivateAccount.as_view(), name='activate-account'),

]