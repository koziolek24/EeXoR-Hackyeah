from django.contrib import admin
from django.urls import path, include
from .views import test_view

urlpatterns = [
    path('test/', test_view),
]
