from django.urls import path
from . import views

urlpatterns = [
    path('', views.TipoIndicadorList.as_view(), name='tipo_indicador_list'),
    path('view/<int:pk>', views.IndicadorList.as_view(), name='indicador_list'),
    path('create/<int:pk>', views.IndicadorCreate.as_view(), name='indicador_new'),
]
