from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Classe que define uma tabela no banco de dados, que representa
# o usuário que tem acesso ao sistema, podendo ser gerente ou vendedor.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    is_vendor = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.user.username
    