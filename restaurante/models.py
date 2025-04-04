from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome_categoria = models.TextField()
    def __str__(self):
        return f"{self.nome_categoria}"
    @staticmethod
    def create_default_values():
        categorias = ['Pizza', 'Café', 'Burger']
        for categoria in categorias:
            if not Categoria.objects.filter(nome_categoria=categoria).exists():
                Categoria.objects.create(nome_categoria=categoria)
    
class Produto(models.Model):
    nome = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"