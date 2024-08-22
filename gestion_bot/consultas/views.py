import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .airtable_integration import obtener_consultas, obtener_consulta, actualizar_en_airtable, crear_en_airtable, eliminar_en_airtable

@csrf_exempt
def lista_consultas(request):
    consultas = obtener_consultas()
    return render(request, 'consultas/lista_consultas.html', {'consultas': consultas})



@csrf_exempt
@require_http_methods(["GET", "PUT"])
def actualizar_estado(request, record_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            estado = data.get('Estado')
            if not estado:
                return JsonResponse({'success': False, 'error': 'El estado no fue proporcionado'}, status=400)
            
            consulta = obtener_consulta(record_id)
            if not consulta:
                return JsonResponse({'success': False, 'error': 'Consulta no encontrada'}, status=404)
            
            consulta['fields']['Estado'] = estado
            if actualizar_en_airtable(consulta):
                return JsonResponse({'success': True, 'newState': estado})
            else:
                return JsonResponse({'success': False, 'error': 'Error al actualizar en Airtable'}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    # Si es GET, devolver el estado actual
    consulta = obtener_consulta(record_id)
    if consulta:
        return JsonResponse({'success': True, 'currentState': consulta['fields'].get('Estado', '')})
    return JsonResponse({'success': False, 'error': 'Consulta no encontrada'}, status=404)

# ... (resto de las vistas)



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
            # Retorna un HTTP 204 No Content que indica que la operación fue exitosa, 
            # pero no se envía ningún contenido de vuelta.
            return JsonResponse({'success': True}, status=204)
    return JsonResponse({'success': False}, status=400)