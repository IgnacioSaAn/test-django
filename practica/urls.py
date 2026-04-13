"""
URL configuration for practica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from cuentas.views import registro, login_view, logout_view, ver_perfil
from notas.views import ver_notas, crear_nota, editar_nota, eliminar_nota, buscar_nota_por_titulo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', ver_perfil, name='perfil'),
    path('notas/', ver_notas, name='ver_notas'),
    path('notas/crear/', crear_nota, name='crear_nota'),
    path('notas/editar/<int:id>/', editar_nota, name='editar_nota'),
    path('notas/eliminar/<int:id>/', eliminar_nota, name='eliminar_nota'),
    path('notas/buscar/', buscar_nota_por_titulo, name='buscar_nota_por_titulo'),
]
