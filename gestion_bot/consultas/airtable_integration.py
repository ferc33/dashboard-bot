from pyairtable import Table
from django.conf import settings

table = Table(settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, "Consultas")

def obtener_consultas():
    try:
        return table.all()
    except Exception as e:
        print(f"Error: {e}")
        return []

def obtener_consulta(airtable_id):
    try:
        return table.get(airtable_id)
    except Exception as e:
        print(f"Error: {e}")
        return None

def actualizar_en_airtable(consulta):
    try:
        table.update(consulta.airtable_id, {
            "Cliente": consulta.Cliente,
            "Telefono": consulta.Telefono,
            "TipoConsulta": consulta.TipoConsulta,
            "Estado": consulta.Estado,
            "DescripcionConsulta": consulta.DescripcionConsulta,
            "Direccion": consulta.Direccion,
        })
        return True
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

def eliminar_en_airtable(airtable_id):
    try:
        table.delete(airtable_id)
        return True
    except Exception as e:
        print(f"Error al eliminar en Airtable: {e}")
        return False
