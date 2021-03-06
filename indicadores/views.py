from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django_tables2 import RequestConfig
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import TipoIndicador, Indicador
from .tables import TipoIndicadorTable, IndicadorTable
from .forms import CustomIndicadorCreationForm

import logging

logger = logging.getLogger(__name__)

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
    template_name = 'indicadores/indicador_list.html'
    model = Indicador
    context_object_name = 'indicador'
    ordering = ['nombre']

    def get_queryset(self):
        tipo_indicador = self.kwargs['tipo_indicador']
        self.request.session['tipo_indicador'] = tipo_indicador
    
    def get_context_data(self, **kwargs):
        context = super(IndicadorList, self).get_context_data(**kwargs)
        tipo_indicador = self.request.session['tipo_indicador']
        table = IndicadorTable(Indicador.objects.all().filter(tipo_indicador_id=tipo_indicador))
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        context['tipo_indicador'] = tipo_indicador
        return context

class IndicadorCreate(LoginRequiredMixin, CreateView):
    model = Indicador
    form_class = CustomIndicadorCreationForm
    success_url = reverse_lazy('indicador_list')
    template_name_suffix = '_create'

    def get_context_data(self, **kwargs):
        context = super(IndicadorCreate, self).get_context_data(**kwargs)
        tipo_indicador = self.request.session['tipo_indicador']
        context['tipo_indicador'] = tipo_indicador
        return context

    def get_form_kwargs(self):
        tipo_indicador = self.request.session.get('tipo_indicador')
        kwargs = super(IndicadorCreate, self).get_form_kwargs()
        kwargs.update({'tipo_indicador': tipo_indicador})
        return kwargs

    def form_valid(self, form):
        response = super(IndicadorCreate, self).form_valid(form)
        #obj_tipo_indicador = TipoIndicador.objects.get(id=tipo_indicador)
        #form.instance.tipo_indicador = obj_tipo_indicador
        #form.save()
        return response  

