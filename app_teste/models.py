from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=200)
    prontuario = models.CharField(verbose_name='Prontuario', max_length=200)
    