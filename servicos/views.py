from django.shortcuts import render

from .models import Servico, Promocao


def servicos(request):
  tipo_veiculo = request.GET.get('tipo_veiculo')
  categoria_servico = request.GET.get('categoria_servico')
  tipo_servico = request.GET.get('tipo_servico')

  context = {
    'tipo_veiculo': tipo_veiculo,
    'categoria_servico': categoria_servico,
    'tipo_servico': tipo_servico
  }

  return render(request, 'servicos/servicos.html', context)

def resultados_servicos(request):
  tipo_veiculo = request.GET.get('tipo_veiculo')
  categoria_servico = request.GET.get('categoria_servico')
  tipo_servico = request.GET.get('tipo_servico')
  buscar = request.GET.get('buscar')

  if (buscar == 'todos'):
    context = {
      'servicos_moto': Servico.objects.all().filter(tipo_veiculo='M'),
      'servicos_carro': Servico.objects.all().filter(tipo_veiculo='C')
    }

  if (tipo_veiculo == 'moto'):
    servicos_moto = Servico.objects.all().filter(tipo_veiculo='M')
    if (categoria_servico == 'simples'):
      servicos_moto = servicos_moto.filter(categoria='SIMPLES')
    elif (categoria_servico == 'detalhado'):
      servicos_moto = servicos_moto.filter(categoria='DETALHADO')

    context = {
      'servicos_moto': servicos_moto
    }

  elif (tipo_veiculo == 'carro'):
    servicos_carro = Servico.objects.all().filter(tipo_veiculo='C')
    if (categoria_servico == 'simples'):
      servicos_carro = servicos_carro.filter(categoria='SIMPLES')
    elif (categoria_servico == 'detalhado'):
      servicos_carro = servicos_carro.filter(categoria='DETALHADO')
      if (tipo_servico == 'interno'):
        servicos_carro = servicos_carro.filter(tipo_servico='INTERNO')
      elif (tipo_servico == 'externo'):
        servicos_carro = servicos_carro.filter(tipo_servico='EXTERNO')
      elif (tipo_servico == 'ambos'):
        pass

    context = {
      'servicos_carro': servicos_carro
    }

  return render(request, 'servicos/resultados-servicos.html', context)


def servico_info(request, id):
  context = {
    'servico': Servico.objects.get(id=id)
  }
  return render(request, 'servicos/servico-info.html', context)

def promocao_info(request, id):
  context = {
    'promocao': Promocao.objects.get(id=id)
  }
  return render(request, 'servicos/promocao-info.html', context)
