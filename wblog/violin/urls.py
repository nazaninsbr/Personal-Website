from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^$', views.postList, name = "index")
]
