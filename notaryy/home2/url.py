from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('sendmail/', views.sendmail),
    path('comment/', views.comment)
]
