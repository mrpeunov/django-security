from django.urls import path
from case3_1.views import get_books_orm, get_books_raw

urlpatterns = [
    path("book/", get_books_orm),
    path("book/raw/", get_books_raw)
]
