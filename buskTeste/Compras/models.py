from django.db import models
from Livros.models import Livro

# Create your models here.

class Compras(models.Model):

    Id = models.CharField(max_length=255, verbose_name="ID", primary_key=True)
    data = models.DateField(verbose_name="Data da Compra", auto_now_add=True)
    fornecedor = models.CharField(max_length=255, verbose_name="Fornecedor", blank=False, null=False, default=" ")
    # livro = models.ForeignKey(Livro, on_delete=models.PROTECT, verbose_name="Livro")
    # preco_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="P.eço Unitário")
    # quantidade = models.IntegerField(verbose_name="Quantidade")
    # preco_total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço Total")
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Subtotal", default=0.00)
    desconto = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Desconto", default=0.00)
    total = models.DecimalField(max_digits=8,decimal_places=2, verbose_name="Preço Total", default=0.00)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return self.Id