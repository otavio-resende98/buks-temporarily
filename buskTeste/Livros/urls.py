from django.urls import path
from .views import register_book, read_book, update_book_form, update_book, delete_book, delete_book_confirm

app_name = "Livros"

urlpatterns = [
    path("register/book", register_book, name="register_book"),
    path("read/book/", read_book, name="read_book"),
    #path("read/book/<str:pk>/", read_book_form, name="read_book_form"),
    path("update/book/", update_book, name="update_book"),
    path("update/book/<str:pk>/", update_book_form, name="update_book_form"),
    path("delete/book/", delete_book, name="delete_book"),
    path("delete/book/<str:pk>/", delete_book_confirm, name="delete_book_confirm"),
]
