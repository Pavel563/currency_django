from django.urls import path
from accounts import views
app_name = 'account'

urlpatterns = [
    path('my-profile/<int:pk>', views.MyProfile.as_view(), name='my-profile'),

]