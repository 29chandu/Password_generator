from django.urls import path

from . import views

generator_urls = [
    path('password/', views.generate_password_view, name='password'),
]