from django.db import models

# Create your models here.

class Estudantes(models.Model):
    nome = models.CharField('Nome', max_length=100)
    ingresso = models.CharField('Ingresso', max_length=6)
    nota = models.IntegerField('Nota')
    situacao = models.CharField('Situação', max_length=10)

    def __str__(self):
        return f'{self.nome} {self.situacao}'




