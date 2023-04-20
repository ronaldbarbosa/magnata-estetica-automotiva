from django.db import models

class Contato(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField()
  assunto = models.CharField(max_length=50)
  mensagem = models.CharField(max_length=300)

# TODO: adicionar data e hora do contato