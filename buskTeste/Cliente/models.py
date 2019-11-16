from django.db import models

# Create your models here.

class Cliente(models.Model):

    cpf = models.CharField(max_length=255, verbose_name="CPF", primary_key=True)
    nome = models.CharField(max_length=255, verbose_name="Nome")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(max_length=255, verbose_name="E-Mail")
    celular = models.CharField(max_length=255, verbose_name="Celular")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.cpf
