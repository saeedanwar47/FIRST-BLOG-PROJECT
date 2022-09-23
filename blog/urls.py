from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>', category)
]
