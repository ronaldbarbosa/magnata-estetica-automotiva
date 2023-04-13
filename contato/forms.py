from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = "__all__"
    labels = {
      'nome': 'Nome',
      'email': 'Email',
      'assunto': 'Assunto',
      'mensagem': 'Mensagem'
    }
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'assunto': forms.TextInput(attrs={'class': 'form-control'}),
      'mensagem': forms.Textarea(attrs={'class': 'form-control'})
    }
