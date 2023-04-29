from django.db import models

TIPO_VEICULO = [
  ('C', 'Carro'),
  ('M', 'Moto')
]

class Servico(models.Model):
  class Meta:
    verbose_name = 'Serviço'
    verbose_name_plural = 'Serviços'

  cliente = models.CharField(max_length=150)
  veiculo = models.CharField(max_length=50)
  tipo_servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE)
  data = models.DateField()
  hora = models.TimeField()
  observacao = models.CharField(max_length=300, blank=True)

class TipoServico(models.Model):
  class Meta:
    verbose_name = 'Tipo de serviço'
    verbose_name_plural = 'Tipos de serviço'

  nome = models.CharField(max_length=100)
  descricao = models.CharField(max_length=500)
  tipo_veiculo = models.CharField(max_length=1, choices=TIPO_VEICULO)
  preco_base = models.DecimalField(max_digits=6, decimal_places=2)
  image = models.ImageField(upload_to='images/')

class Promocao(models.Model):
  class Meta:
    verbose_name = 'Promoção'
    verbose_name_plural = 'Promoções'

  tipo_servico = models.ForeignKey('TipoServico', on_delete=models.CASCADE)
  preco_promocao = models.DecimalField(max_digits=6, decimal_places=2)
  valido_ate = models.DateField()
