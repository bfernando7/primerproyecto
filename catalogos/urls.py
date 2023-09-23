from django.urls import path
from .views import *

urlpatterns = [
    path('paises/', PaisListView.as_view(), name='pais_list'),
    path('paises/nuevo/', PaisCreateView.as_view(), name='pais_create'),
    path('departamentos/nuevo/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('paises/<int:pk>/', PaisUpdateView.as_view(), name='pais_update'),
    path('paises/<int:pk>/eliminar/', PaisDeleteView.as_view(), name='pais_delete'),
    path('departamentos/', DepartamentoListView.as_view(), name='departamento_list'),
    path('departamentos/<int:pk>/eliminar/', DepartamentoDeleteView.as_view(), name='departamento_delete'),
    path('departamentos/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('municipios/', MunicipioListView.as_view(), name='municipio_list'),
    path('municipios/<int:pk>/eliminar/', MunicipioDeleteView.as_view(), name='municipio_delete'),
    path('municipios/<int:pk>/', MunicipioUpdateView.as_view(), name='municipio_update'),
     path('municipios/nuevo/', MunicipioCreateView.as_view(), name='municipio_create'),

]
