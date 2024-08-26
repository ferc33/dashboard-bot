from pyairtable import Table
from django.conf import settings

table = Table(settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, "Consultas")

def obtener_consultas():
    try:
        records = table.all()
        for record in records:
            # Asegúrate de que el record_id se agrega correctamente
            record['record_id'] = record['id']
        return records
    except Exception as e:
        print(f"Error al obtener consultas: {e}")
        return []


def obtener_consulta(record_id):
    try:
        return table.get(record_id)
    except Exception as e:
        print(f"Error: {e}")
        return None

def actualizar_en_airtable(consulta):
    try:
        record_id = consulta['id']  # Obtener el ID del registro
        fields = {
            "Cliente": consulta['fields'].get('Cliente', ''),
            "Telefono": consulta['fields'].get('Telefono', ''),
            "TipoConsulta": consulta['fields'].get('TipoConsulta', ''),
            "Estado": consulta['fields'].get('Estado', ''),
            "DescripcionConsulta": consulta['fields'].get('DescripcionConsulta', ''),
            "Direccion": consulta['fields'].get('Direccion', '')
        }
        
        # Realiza la actualización en Airtable usando el ID del registro
        response = table.update(record_id, fields)
        
        # Imprime la respuesta para verificar si la actualización fue exitosa
        print(f"Respuesta de Airtable: {response}")
        
        return True if response else False
    except Exception as e:
        print(f"Error al actualizar en Airtable: {e}")
        return False


def crear_en_airtable(consulta_data):
    try:
        new_record = table.create(consulta_data)
        return new_record
    except Exception as e:
        print(f"Error al crear en Airtable: {e}")
        return None

def eliminar_en_airtable(record_id):
    try:
        table.delete(record_id)
        return True
    except Exception as e:
        print(f"Error al eliminar en Airtable: {e}")
        return False
