from django.conf.urls import url
from . import views
from django.urls import path

app_name='login'
urlpatterns = [
    path('', views.index, name='login'),


    ]