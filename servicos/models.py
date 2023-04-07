from django.db import models

class Servico(models.Model):
  TIPO_VEICULO = [
    ('C', 'Carro'),
    ('M', 'Moto')
  ]

  cliente = models.CharField(max_length=150)
  veiculo = models.CharField(max_length=50)
  tipo_veiculo = models.CharField(max_length=1, choices=TIPO_VEICULO)
  tipo_servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE)
  data = models.DateField()
  hora = models.TimeField()
  observacao = models.CharField(max_length=300, blank=True)

class TipoServico(models.Model):
  nome = models.CharField(max_length=100)
  preco_base = models.DecimalField(max_digits=6, decimal_places=2)
  img_url = models.URLField()