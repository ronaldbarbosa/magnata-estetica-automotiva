from django.contrib import admin

from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
  list_display = ['nome', 'assunto', 'data']
  list_filter = ['data']
