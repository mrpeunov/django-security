from django.urls import path
from case2_2.views import create_post

urlpatterns = [
    path("post/", create_post)
]
