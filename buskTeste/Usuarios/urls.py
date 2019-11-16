from django.urls import path
from .views import login

app_name = "Usuarios"

urlpatterns = [
     path("login/", login, name="login"),
] 