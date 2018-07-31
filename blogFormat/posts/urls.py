from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_home, name="blog"),
    path('<int:id>/', views.post_detail, name="blog_detail"),
    path('create/', views.post_create, name="blog_create"),
    path('update/', views.post_update, name="blog_update"),
    path('delete/', views.post_delete, name="blog_delete"),
]