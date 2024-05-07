from django.db import models

class Hotel(models.Model):
    # ID de hotel, a menudo es recomendable usar el campo AutoField como clave primaria
    objects = None
    idHotel = models.CharField(max_length=100, primary_key=True)

    # Nombre del establecimiento
    nombreEstablecimiento = models.CharField(max_length=100)

    # Horarios de check-in y check-out
    horaCheckIn = models.TimeField()
    horaCheckOut = models.TimeField()

    # Pet-friendly, generalmente se usa un campo booleano para representar sí/no
    petFriendly = models.BooleanField()

    # Servicios del hotel
    servicio = models.CharField(max_length=100)

    # Dirección: interior y exterior
    numeroInterior = models.CharField(max_length=100, blank=True, null=True)  # Puede ser null o vacío
    numeroExterior = models.IntegerField()

    # Dirección: colonia, calle, estado
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreEstablecimiento



