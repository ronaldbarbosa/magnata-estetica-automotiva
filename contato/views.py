from django.shortcuts import render
from twilio.rest import Client
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
    form_assunto = form.cleaned_data['assunto']
    form_mensagem = form.cleaned_data['mensagem']

    contato = Contato(
      nome=form_nome,
      email=form_email,
      assunto=form_assunto,
      mensagem=form_mensagem
    )

    contato.save()
    enviar_mensagem(contato)

    return render(request, 'contato/contato.html', {
      'form': ContatoForm,
      'enviado': True
    })

def enviar_mensagem(contato):
  account_sid = config('TWILIO_SID')
  auth_token = config('TWILIO_AUTH_TOKEN')
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    from_=config('TWILIO_FROM'),
    body=f'Magnata: {contato.mensagem}',
    to=config('TWILIO_TO')
  )
