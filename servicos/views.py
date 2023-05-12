from django.shortcuts import render

from .models import Servico
def servicos(request):
  servicos_carro = Servico.objects.all().filter(tipo_veiculo='C')
  servicos_moto = Servico.objects.all().filter(tipo_veiculo='M')

  # print(servicos_carro)
  # print(servicos_carro.order_by('categoria'))

  return render(request, 'servicos/servicos.html', {
    'servicos_carro': servicos_carro,
    'servicos_moto': servicos_moto
  })
