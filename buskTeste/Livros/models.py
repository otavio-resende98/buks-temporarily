from django.db import models

# Create your models here.

# Classe que define uma tabela no banco de dados representando um Livro,
# que pode ser cadastradoo, alterado, consultado e excluído do sistema.
class Livro(models.Model):

    isbn = models.CharField(
        max_length=255, verbose_name="ISBN", primary_key=True)
    capa = models.ImageField(upload_to='media', verbose_name='Capa')
    titulo = models.CharField(max_length=255, verbose_name="Título")
    subtitulo = models.CharField(max_length=255, verbose_name="Subtítulo")
    autor = models.CharField(max_length=255, verbose_name="Autor")
    editora = models.CharField(max_length=255, verbose_name="Editora")
    edicao = models.CharField(max_length=255, verbose_name="Edição")
    ano = models.CharField(max_length=255, verbose_name="Ano")
    paginas = models.CharField(max_length=255, verbose_name="Nº de Páginas")
    genero = models.CharField(max_length=255, verbose_name="Gênero")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade")
    novo = models.BooleanField(verbose_name="Novo", default=False)
    sinopse = models.CharField(max_length=255, verbose_name="Sinopse")
    preco_compra = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Preço de compra")
    preco_venda = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Preço de venda")

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.titulo
