from django.shortcuts import render
from .airtable_integration import obtener_consultas
from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta

from .airtable_integration import actualizar_en_airtable

def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})




def actualizar_estado(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        consulta.Estado = nuevo_estado
        consulta.save()
        actualizar_en_airtable(consulta)
        return redirect('lista_consultas')

