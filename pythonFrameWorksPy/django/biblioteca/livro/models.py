from django.db import models
from usuarios.models import Usuario

class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
    
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'
    
    def __str__(self):
        return self.nome
    
class Emprestimos(models.Model):
    mome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True)
    mome_emprestado_anonimo = models.CharField(max_length=30, null=True, blank=True)
    data_emprestimo = models.DateField(null=True, blank=True)
    data_devolucao = models.DateField(null=True, blank=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.mome_emprestado} | {self.livro}"