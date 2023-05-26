from django.contrib import admin

from .models import Demanda, Servico, Promocao

# @admin.register(Demanda)
# class DemandaAdmin(admin.ModelAdmin):
#   list_display = ('cliente', 'veiculo', 'tipo_servico')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
  list_display = ('nome', 'preco_base')
  list_filter = ('categoria', 'tipo_servico', 'tipo_veiculo')

@admin.register(Promocao)
class PromocaoAdmin(admin.ModelAdmin):

  list_display = ('servico', 'preco_promocao', 'valido_ate')
