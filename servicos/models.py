from cloudinary.models import CloudinaryField
from django.db import models

TIPO_VEICULO = [
    ('C', 'Carro'),
    ('M', 'Moto')
]

CATEGORIA_SERVICO = [
    ('SIMPLES', 'Simples'),
    ('TECNICO', 'Técnico')
]

TIPO_SERVICO = [
    ('INTERNO', 'Interno'),
    ('EXTERNO', 'Externo'),
    ('AMBOS', 'Ambos')
]


class Demanda(models.Model):
    class Meta:
        verbose_name = 'Demanda'
        verbose_name_plural = 'Demandas'

    cliente = models.CharField(max_length=150)
    veiculo = models.CharField(max_length=50)
    tipo_servico = models.ForeignKey('Servico', on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    observacao = models.CharField(max_length=300, blank=True)


class Servico(models.Model):
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=500)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_SERVICO)
    tipo_servico = models.CharField(max_length=10, choices=TIPO_SERVICO, verbose_name='Tipo de serviço')
    tipo_veiculo = models.CharField(max_length=1, choices=TIPO_VEICULO, verbose_name='Tipo de veículo')
    preco_base = models.DecimalField(max_digits=6, decimal_places=2)
    imagem = CloudinaryField('image')
    video = CloudinaryField('video', blank=True)

    def __str__(self):
        return f'{self.nome}'


class Promocao(models.Model):
    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'

    servico = models.ForeignKey('Servico', on_delete=models.CASCADE, null=True)
    descricao = models.CharField(max_length=300, default='')
    preco_promocao = models.DecimalField(max_digits=6, decimal_places=2)
    valido_ate = models.DateField()

    def __str__(self):
        return f'Promoção {self.servico}'
