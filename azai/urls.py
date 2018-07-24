"""azai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomAuthForm, CustomPasswordResetForm

urlpatterns = [
    path('', RedirectView.as_view(url='/azai', permanent=True)),
    path('azai/cuentas/login/', auth_views.login, name='login', kwargs={"authentication_form": CustomAuthForm}),
    path('azai/cuentas/password_reset/', auth_views.password_reset, name='password_reset', kwargs={"password_reset_form": CustomPasswordResetForm}),

    path('azai/', views.HomePageView.as_view(), name='home'),
    path('azai/admin/', admin.site.urls),
    path('azai/usuarios/', include('usuarios.urls')),
    path('azai/cuentas/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
