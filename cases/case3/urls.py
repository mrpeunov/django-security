from django.urls import path
from case3.views import create_post, get_post

urlpatterns = [
    path("create_post/", create_post),
    path("get_post/", get_post)
]
