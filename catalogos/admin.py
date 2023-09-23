from django.contrib import admin
from .models import Pais, Departamento, Municipio


class PaisAdmin(admin.ModelAdmin):
    list_display = ['nombre']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pais', 'active']
    list_filter = ['pais__nombre', 'active']
    search_fields = ['nombre', 'pais__nombre']



class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'codigo', 'active')
    list_filter = ('departamento__nombre', 'active')
    search_fields = ('nombre', 'departamento__nombre', 'departamento__pais__nombre')

   

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Municipio,MunicipioAdmin)

