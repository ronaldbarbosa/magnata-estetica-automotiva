from django.shortcuts import render

from .models import TipoServico
def servicos(request):
  return render(request, 'servicos/servicos.html', {
    'servicos': TipoServico.objects.all(),
  })
