from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consultas/actualizar/<str:id>/', views.actualizar_estado, name='actualizar_estado'),
]
