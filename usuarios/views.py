from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Usuario

# Create your views here.
class UsuarioList(ListView):
    model = Usuario

class UsuarioView(DetailView):
    model = Usuario

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['grupo', 'email', 'first_name', 'last_name', 'numero_identificacion', 'telefono', 'ocupacion', 'is_active', 'is_staff']
    template_name_suffix = '_create'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['grupo', 'email', 'first_name', 'last_name', 'numero_identificacion', 'telefono', 'ocupacion', 'is_active', 'is_staff']
    success_url = reverse_lazy('usuario_list')

class UsuarioDelete(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario_list')