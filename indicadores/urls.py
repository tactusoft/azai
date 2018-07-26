from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.TipoIndicadorList.as_view(), name='tipo_indicador_list'),
    url(r'^view/(?P<tipo_indicador>[0-9]+)/$', views.IndicadorList.as_view(), name='indicador_list'),
    path('create/<int:pk>', views.IndicadorCreate.as_view(), name='indicador_new'),
]
