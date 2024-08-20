from .airtable_integration import obtener_consultas, actualizar_en_airtable
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Consulta
from django.views.decorators.csrf import csrf_exempt

def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})

@csrf_exempt
def actualizar_estado(request, id):
    if request.method == 'POST':
        # Asegúrate de que 'id' sea el ID numérico
        consulta = get_object_or_404(Consulta, pk=id)
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in ['Pendiente', 'En proceso', 'Finalizado']:
            consulta.estado = nuevo_estado
            consulta.save()
            return redirect('lista_consultas')
    return HttpResponse("Método no permitido", status=405)


@csrf_exempt
def borrar_consulta(request, id):
    if request.method == "POST":
        consulta = get_object_or_404(Consulta, pk=id)
        consulta.delete()
        return redirect('lista_consultas')
    return HttpResponse("Método no permitido", status=405)
