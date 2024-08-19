from django.shortcuts import render
from .airtable_integration import obtener_consultas
from django.shortcuts import render, get_object_or_404, redirect

def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})


def actualizar_estado(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    # Aquí puedes actualizar el estado de la consulta. Por ejemplo:
    consulta.estado = 'Finalizado'  # Cambia 'Nuevo Estado' por el estado que desees asignar.
    consulta.save()
    return redirect('lista_consultas')  # Redirige a la lista de consultas después de actualizar
