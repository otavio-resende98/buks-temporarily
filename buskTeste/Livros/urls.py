from django.urls import path
from .views import register_book, read_book, update_book_form, update_book

app_name = "Livros"

urlpatterns = [
    path("register/book", register_book, name="register_book"),
    path("read/book/", read_book, name="read_book"),
    path("update/book/", update_book, name="update_book"),
    path("update/book/<str:pk>/", update_book_form, name="update_book_form"),
]
