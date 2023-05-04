from django.core.validators import MinLengthValidator
from django.db import models

class Contato(models.Model):
  nome = models.CharField(max_length=50)
  email = models.EmailField(blank=True)
  celular = models.CharField(max_length=15, validators=[MinLengthValidator(15)])
  assunto = models.CharField(max_length=50)
  mensagem = models.TextField(max_length=300)
  data = models.DateTimeField(auto_now_add=True)
# TODO: adicionar data e hora do contato
