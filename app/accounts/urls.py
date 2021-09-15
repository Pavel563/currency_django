from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views



app_name = 'account'

urlpatterns = [
    path('my-profile/', views.MyProfile.as_view(), name='my-profile'),
    path('signup/', views.SingUp.as_view(), name='signup'),
    path('activate/account/<uuid:activation_key>', views.ActivateAccount.as_view(), name='activate-account'),

    path('password_reset/', auth_views.PasswordResetView, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    path('reset/<uuid>', auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]