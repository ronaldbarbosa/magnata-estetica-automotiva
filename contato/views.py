from django.shortcuts import render

from .forms import ContatoForm
from .models import Contato

def contato(request):
  if request.method == 'GET':
    return render(request, 'contato/contato.html', {
      'form': ContatoForm,
      'enviado': False
    })

  form = ContatoForm(request.POST)
  if form.is_valid():
    form_nome = form.cleaned_data['nome']
    form_email = form.cleaned_data['email']
    form_assunto = form.cleaned_data['assunto']
    form_mensagem = form.cleaned_data['mensagem']

    contato = Contato(
      nome=form_nome,
      email=form_email,
      assunto=form_assunto,
      mensagem=form_mensagem
    )

    contato.save()

    return render(request, 'contato/contato.html', {
      'form': ContatoForm,
      'enviado': True
    })
