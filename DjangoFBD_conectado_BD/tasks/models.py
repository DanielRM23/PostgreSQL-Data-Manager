from django.db import models

class Hotel(models.Model):
    idhotel = models.CharField(max_length=100, primary_key=True)  # Usar el nombre exacto
    nombreestablecimiento = models.CharField(max_length=100)

    # Otros campos, según la estructura de la base de datos
    horacheckin = models.TimeField()
    horacheckout = models.TimeField()
    petfriendly = models.CharField(max_length=2)  # Cambiar según la base de datos
    servicio = models.CharField(max_length=100)
    numerointerior = models.CharField(max_length=100, blank=True, null=True)
    numeroexterior = models.IntegerField()
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreestablecimiento

    class Meta:
        db_table = 'hotel'  # Asegura que apunte a la tabla correcta
