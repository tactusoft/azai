from django.urls import path
from . import views

urlpatterns = [
    path('', views.UsuarioList.as_view(), name='usuario_list'),
    path('new', views.UsuarioCreate.as_view(), name='usuario_new'),
    path('view/<int:pk>', views.UsuarioView.as_view(), name='usuario_view'),
    path('edit/<int:pk>', views.UsuarioUpdate.as_view(), name='usuario_edit'),
    path('delete/<int:pk>', views.UsuarioDelete.as_view(), name='usuario_delete'),
]
