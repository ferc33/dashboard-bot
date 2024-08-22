import json
from .airtable_integration import obtener_consultas, obtener_consulta, actualizar_en_airtable, crear_en_airtable, eliminar_en_airtable
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

@csrf_exempt
def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})


@csrf_exempt
def actualizar_estado(request, record_id):
    if request.method == "PUT":
        estado = request.POST.get('Estado')
        
        if estado:
            consulta = obtener_consulta(record_id)
            if consulta:
                consulta['fields']['Estado'] = estado
                if actualizar_en_airtable(consulta):
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False, 'error': 'Error al actualizar en Airtable'}, status=500)
            else:
                return JsonResponse({'success': False, 'error': 'Consulta no encontrada'}, status=404)
        else:
            return JsonResponse({'success': False, 'error': 'El estado no fue proporcionado'}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=400)

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
def borrar_consulta(request, record_id):
    if request.method == "DELETE":
        if eliminar_en_airtable(record_id):
            return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)
