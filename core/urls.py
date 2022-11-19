# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
# from apps.api.urls import router



urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    # path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes 
    path("", include("apps.api.urls")),
    # path('persons', include(router.urls)),

    # Leave `Home.Urls` as last the last line
    # path("", include("apps.home.urls"))
]
