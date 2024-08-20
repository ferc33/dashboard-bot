
from pyairtable import Table
from django.conf import settings

table = Table(settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, "Consultas")

def obtener_consultas():
    try:
        return table.all()
    except Exception as e:
        print(f"Error: {e}")
        return []

def actualizar_en_airtable(consulta):
    api_key = config('AIRTABLE_API_KEY')
    base_id = config('AIRTABLE_BASE_ID')
    table_name = "Consultas"

    url = f"https://api.airtable.com/v0/{base_id}/{table_name}/{consulta.id}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "fields": {
            "Cliente": consulta.Cliente,
            "Telefono": consulta.Telefono,
            "TipoConsulta": consulta.TipoConsulta,
            "Estado": consulta.Estado,
            "DescripcionConsulta": consulta.DescripcionConsulta,
            "Direccion": consulta.Direccion,
            "external_id": consulta.external_id,
        }
    }

    response = requests.patch(url, json=data, headers=headers)

    if response.status_code == 200:
        print("Datos actualizados en Airtable con éxito.")
    else:
        print(f"Error al actualizar en Airtable: {response.status_code}")
