from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = "__all__"
    labels = {
      'nome': 'Nome',
      'email': 'Email',
      'celular': 'Celular',
      'assunto': 'Assunto',
      'mensagem': 'Mensagem',
      'data': 'Data'
    }
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'celular': forms.TextInput(attrs={'class': 'form-control celular'}),
      'assunto': forms.TextInput(attrs={'class': 'form-control'}),
      'mensagem': forms.Textarea(attrs={'class': 'form-control'})
    }
