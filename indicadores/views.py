from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django_tables2 import RequestConfig
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TipoIndicador, Indicador
from .tables import TipoIndicadorTable, IndicadorTable
from .forms import CustomIndicadorCreationForm

# Create your views here.
class TipoIndicadorList(LoginRequiredMixin, ListView):
    model = TipoIndicador
    context_object_name = 'tipo_indicador'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super(TipoIndicadorList, self).get_context_data(**kwargs)
        table = TipoIndicadorTable(TipoIndicador.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

class IndicadorList(LoginRequiredMixin, ListView):
    model = Indicador
    context_object_name = 'indicador'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super(IndicadorList, self).get_context_data(**kwargs)
        table = IndicadorTable(Indicador.objects.all().filter(tipo_indicador_id=1))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context

class IndicadorCreate(LoginRequiredMixin, CreateView):
    model = Indicador
    form_class = CustomIndicadorCreationForm
    success_url = reverse_lazy('indicador_list')
    template_name_suffix = '_create'

