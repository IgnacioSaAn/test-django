from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    #Uso de ejemplo para class Based Views
    #esta en vez de llamarse solo por el nombre de la funcion, se la llama con el nombre de la clase y el as_view()
    path('', views.VerNotasView.as_view(), name='ver_notas'),
    path('crear/', views.crear_nota, name='crear_nota'),
    path('editar/<int:id>/', views.editar_nota, name='editar_nota'),
    path('eliminar/<int:id>/', views.eliminar_nota, name='eliminar_nota'),
    path('buscar/', views.buscar_nota_por_titulo, name='buscar_nota_por_titulo'),
]