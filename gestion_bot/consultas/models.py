from django.db import models



class Consulta(models.Model):
    nombre_de_cliente = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    tipo_de_consulta = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    descripcion = models.TextField()
    direccion = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_de_cliente
