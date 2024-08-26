from django.urls import path, include


from . import views
from core.dashboard_bot.views import report
from .views import report, actualizar_estado, crear_consulta, borrar_consulta

urlpatterns = [
     path('consultas/', report, name='report'),
     path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
     path('consultas/actualizar/<str:record_id>/', actualizar_estado, name='actualizar_estado'),
     path('consultas/borrar/<str:record_id>/', borrar_consulta, name='borrar_consulta'),
]

