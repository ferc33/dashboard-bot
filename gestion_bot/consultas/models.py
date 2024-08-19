from django.db import models



class Consulta(models.Model):
    Cliente = models.CharField(max_length=255)
    Telefono = models.CharField(max_length=20)
    TipoConsulta = models.CharField(max_length=50)
    Estado = models.CharField(max_length=50)
    DescripcionConsulta = models.TextField()
    Direccion = models.CharField(max_length=255)
    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Cliente} - {self.TipoConsulta}"

    def to_dict(self):
        return {
            "Cliente": self.Cliente,
            "Telefono": self.Telefono,
            "TipoConsulta": self.TipoConsulta,
            "Estado": self.Estado,
            "DescripcionConsulta": self.DescripcionConsulta,
            "Direccion": self.Direccion,
            "Fecha": self.Fecha,
        }

