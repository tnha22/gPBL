from rest_framework import routers, viewsets
from home.views import PersonViewSet, ListPersonView, CreatePersonView, UpdateDeletePersonView
from django.urls import path, include
from django.conf.urls import url

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'persons', PersonViewSet)

urlpatterns = [
    url(r'api/persons', ListPersonView.as_view(), name="Get all persons"),
    url(r'api/persons/<int:pk>', UpdateDeletePersonView.as_view(), name="update and delete persons"),
    url(r'api/createPerson', CreatePersonView.as_view(), name="create person"),
]