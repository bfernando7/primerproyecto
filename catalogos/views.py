from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pais, Departamento, Municipio
from .forms import PaisForm, DepartamentoForm, MunicipioForm
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator

from .serializers import PaisSerializer
from .serializers import DepartamentoSerializer
from .serializers import MunicipioSerializer

class PaisListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Pais
    template_name = 'pais/pais_list.html'
    context_object_name = 'paises'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.view_pais'
    paginate_by = 5

    def get_queryset(self):
        # Aplicar la búsqueda si se proporciona un término de búsqueda en la URL
        query = self.request.GET.get('q')
        if query:
            return Pais.objects.filter(nombre__icontains=query)
        else:
            return Pais.objects.all()


class DepartamentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Departamento
    template_name = 'departamento/departamento_list.html'
    context_object_name = 'departamentos'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos_view_departamento'
    paginate_by = 5

    def get_queryset(self):
        # Aplicar la búsqueda si se proporciona un término de búsqueda en la URL
        query = self.request.GET.get('q')
        if query:
            return Departamento.objects.filter(nombre__icontains=query)
        else:
            return Departamento.objects.all()


class MunicipioListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Municipio
    template_name = 'municipio/municipio_list.html'
    context_object_name = 'municipios'
    login_url = reverse_lazy('login')
    permission_required = 'catalogos_view_municipio'
    paginate_by = 5

    def get_queryset(self):
        # Aplicar la búsqueda si se proporciona un término de búsqueda en la URL
        query = self.request.GET.get('q')
        if query:
            return Municipio.objects.filter(nombre__icontains=query)
        else:
            return Municipio.objects.all()
        


class PaisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_pais'


class DepartamentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_departamento'


class MunicipioCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')
    permission_required = 'catalogos.add_Municipio'


class PaisUpdateView(LoginRequiredMixin, UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/pais_form.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')


class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'departamento/departamento_form.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')


class MunicipioUpdateView(LoginRequiredMixin, UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'municipio/municipio_form.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')



class PaisDeleteView(LoginRequiredMixin, DeleteView):
    model = Pais
    template_name = 'pais/pais_confirm_delete.html'
    success_url = reverse_lazy('pais_list')
    login_url = reverse_lazy('login')


class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_confirm_delete.html'
    success_url = reverse_lazy('departamento_list')
    login_url = reverse_lazy('login')


class MunicipioDeleteView(LoginRequiredMixin, DeleteView):
    model = Municipio
    template_name = 'municipio/municipio_confirm_delete.html'
    success_url = reverse_lazy('municipio_list')
    login_url = reverse_lazy('login')


    
# viewset para pais


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]



class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]