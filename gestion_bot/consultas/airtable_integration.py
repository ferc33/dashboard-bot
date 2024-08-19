
from pyairtable import Table
from django.conf import settings

table = Table(settings.AIRTABLE_API_KEY, settings.AIRTABLE_BASE_ID, "Consultas")

def obtener_consultas():
    try:
        return table.all()
    except Exception as e:
        print(f"Error: {e}")
        return []
