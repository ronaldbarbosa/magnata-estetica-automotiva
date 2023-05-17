from django.shortcuts import render

from .models import Servico
def servicos(request):
  servicos_carro = Servico.objects.all().filter(tipo_veiculo='C')
  servicos_moto = Servico.objects.all().filter(tipo_veiculo='M')

  context = {
    'servicos_carro': servicos_carro,
    'servicos_moto': servicos_moto
  }

  return render(request, 'servicos/servicos.html', context)

def servico_info(request, id):
  context = {
    'servico': Servico.objects.get(id=id)
  }
  return render(request, 'servicos/servico-info.html', context)
