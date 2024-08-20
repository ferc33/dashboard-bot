from django.urls import path
from . import views


urlpatterns = [
  path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('actualizar/<str:id>/', views.actualizar_estado, name='actualizar_estado'),
    path('borrar/<str:id>/', views.borrar_consulta, name='borrar_consulta'),

 ]


