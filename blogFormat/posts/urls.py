from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_home, name="blog"),
    path('/detail/', views.post_detail, name="detail"),
    path('/create/', views.post_create, name="create"),
    path('/update/', views.post_update, name="update"),
    path('/delete/', views.post_delete, name="delete"),
]