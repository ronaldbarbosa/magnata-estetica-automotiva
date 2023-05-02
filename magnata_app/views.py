from django.shortcuts import render

from servicos.models import Promocao, TipoServico


def index(request):
    promocoes = Promocao.objects.all()
    servicos = TipoServico.objects.all()[:5]


    if promocoes and servicos:
        return render(request, 'magnata_app/index.html', {
            'promocoes': promocoes,
            'servicos': servicos
        })
    if promocoes:
        return render(request, 'magnata_app/index.html', {
            'promocoes': promocoes
        })
    if servicos:
        return render(request, 'magnata_app/index.html', {
            'servicos': servicos
        })
    return render(request, 'magnata_app/index.html')
