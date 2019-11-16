from django.urls import path
from .views import register_purchase

app_name = "Compras"

urlpatterns = [
    path('register/purchase', register_purchase, name="register_purchase"),
]
