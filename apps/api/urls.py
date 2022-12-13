from apps.api.views import * # UserDetailAPI, RegisterUserAPIView,GetHistoryLog, LoginUserView, ListCreateShiftView, UpdateDeleteShiftView,UserList,ListCreateCameraView,UpdateDeleteCameraView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = [
    path("user/<int:pk>", UserDetailAPI.as_view(), name='get-details'),
    path('user/<int:pk>/shift', GetUserShift.as_view(), name='get-user-shift'),
    path("user", UserList.as_view(), name='get-list'),
    path('login', LoginUserView.as_view(), name='login user'),
    path('register', RegisterUserAPIView.as_view(), name='register user'),
    path('shifts', ListCreateShiftView.as_view(), name='shift create'),
    path('shifts/<int:pk>', UpdateDeleteShiftView.as_view(), name='shift edit'),
    path('camera-create', ListCreateCameraView.as_view(),name='camera create'),
    path('cameras/<int:pk>', UpdateDeleteCameraView.as_view(),name='camera edit'),
    path('get-history-log', GetHistoryLog.as_view(),name='get history log'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)