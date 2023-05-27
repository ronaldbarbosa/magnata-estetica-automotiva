from django.urls import path

from . import views

urlpatterns = [
  path('', views.servicos, name='servicos'),
  path('resultados', views.resultados_servicos, name='resultados'),
  path('servico-info/<int:id>', views.servico_info, name='servico_info')
]