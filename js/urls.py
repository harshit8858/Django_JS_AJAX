from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^add/', add, name="add"),
    url(r'^search/', search, name="search"),
]
