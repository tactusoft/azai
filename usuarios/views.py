from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import RequestConfig
from .models import Usuario
from .forms import (CustomUserCreationForm, CustomUserChangeForm)
from .tables import UsuarioTable

# Create your views here.


class UsuarioList(LoginRequiredMixin, ListView,):
    model = Usuario
    context_object_name = 'usuario'
    ordering = ['email']

    def get_context_data(self, **kwargs):
        context = super(UsuarioList, self).get_context_data(**kwargs)
        context['nav_customer'] = True
        table = UsuarioTable(Usuario.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

class UsuarioView(LoginRequiredMixin, DetailView):
    model = Usuario


class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('usuario_list')
    template_name_suffix = '_create'


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('usuario_list')


class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario_list')
