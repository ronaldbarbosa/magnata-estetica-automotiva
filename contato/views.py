from django.shortcuts import render
from django.core.mail import send_mail
from decouple import config

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
    form_celular = form.cleaned_data['celular']
    form_assunto = form.cleaned_data['assunto']
    form_mensagem = form.cleaned_data['mensagem']

    contato = Contato(
      nome=form_nome,
      email=form_email,
      celular=form_celular,
      assunto=form_assunto,
      mensagem=form_mensagem
    )

    contato.save()
    sucesso = enviar_email(contato)

    if sucesso != 0:
      return render(request, 'contato/contato-resultado.html', {
        'enviado': 'sucesso'
      })
    else:
      return render(request, 'contato/contato-resultado.html', {
        'enviado': 'erro'
      })

def enviar_email(contato):
  try:
    return send_mail(contato.assunto, contato.mensagem, config('EMAIL_FROM'), [config('EMAIL_TO')], True)
  except:
    return 0
