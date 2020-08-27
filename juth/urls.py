from django.urls import path

from juth import views

urlpatterns = [
    path('login', views.xhr_login, name='login'),
]
