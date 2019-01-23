from django.db import models

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=20, default='')
    logradouro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100) #Equivalente a cidade
    bairro = models.CharField(max_length=200)
    uf = models.CharField(max_length=100)

    def __str__(self):
        return self.logradouro