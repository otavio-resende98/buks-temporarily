from django.urls import path
from .views import register_client

app_name = "Cliente"

urlpatterns = [
    path('register/client', register_client, name="register_client"),
]
