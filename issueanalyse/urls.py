from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.dashboard, name='Issue Analyse'),
    path('api/analyse/<str:text>', views.analyseIfIsBug),
]
