from django.contrib import admin

from .models import Servico, TipoServico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
  list_display = ('cliente', 'veiculo', 'tipo_servico')

@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):
  list_display = ('nome', 'preco_base')
