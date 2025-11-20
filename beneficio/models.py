from django.db import models

class beneficio(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"beneficio desde {self.fecha_inicio} {'(Activo)' if self.activo else '(Inactivo)'}"