from apps.api.views import UserDetailAPI, RegisterUserAPIView, LoginUserView
from django.urls import path

# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = [
    path("api/get-details", UserDetailAPI.as_view(), name='get-details'),
    path('api/login', LoginUserView.as_view(), name='login user'),
    path('api/register', RegisterUserAPIView.as_view(), name='register user'),

]