from .airtable_integration import obtener_consultas, obtener_consulta, actualizar_en_airtable, crear_en_airtable, eliminar_en_airtable
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .models import Consulta
from django.views.decorators.csrf import csrf_exempt

def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})

@csrf_exempt
def actualizar_estado(request, id):
    consulta = obtener_consulta(id)
    if consulta and request.method == 'POST':
        nuevo_estado = request.POST.get('Estado')
        consulta['fields']['Estado'] = nuevo_estado
        if actualizar_en_airtable(consulta):
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def crear_consulta(request):
    if request.method == 'POST':
        consulta_data = {
            "Cliente": request.POST.get('Cliente'),
            "Telefono": request.POST.get('Telefono'),
            "TipoConsulta": request.POST.get('TipoConsulta'),
            "Estado": request.POST.get('Estado'),
            "DescripcionConsulta": request.POST.get('DescripcionConsulta'),
            "Direccion": request.POST.get('Direccion'),
        }
        new_record = crear_en_airtable(consulta_data)
        if new_record:
            return JsonResponse({'success': True, 'airtable_id': new_record['id']})
    return JsonResponse({'success': False}, status=400)

@csrf_exempt
def borrar_consulta(request, id):
    if request.method == "DELETE":
        if eliminar_en_airtable(id):
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
