from django.shortcuts import render

from .models import Servico
def servicos(request):
  return render(request, 'servicos/servicos.html', {
    'servicos': Servico.objects.all(),
  })
