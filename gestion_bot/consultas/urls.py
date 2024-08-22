from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
    path('consultas/actualizar/<str:id>/', views.actualizar_estado, name='actualizar_estado'),
    path('consultas/borrar/<str:id>/', views.borrar_consulta, name='borrar_consulta'),
]
