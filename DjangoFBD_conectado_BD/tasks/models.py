from django.db import models

class Hotel(models.Model):
    """
    Modelo para representar un hotel en la base de datos.

    Atributos:
        idhotel (str): Identificador único del hotel. Usado como clave primaria.
        nombreestablecimiento (str): Nombre del establecimiento del hotel.
        horacheckin (time): Hora estándar de check-in del hotel.
        horacheckout (time): Hora estándar de check-out del hotel.
        petfriendly (str): Indica si el hotel admite mascotas. Ejemplo: 'S' para sí, 'N' para no.
        servicio (str): Tipo de servicio que ofrece el hotel.
        numerointerior (str, opcional): Número interior del hotel. Puede ser nulo.
        numeroexterior (int): Número exterior del hotel.
        colonia (str): Nombre de la colonia donde está ubicado el hotel.
        calle (str): Calle donde está ubicado el hotel.
        estado (str): Estado donde está ubicado el hotel.

    Métodos:
        __str__(): Retorna una representación en cadena del nombre del establecimiento.

    Meta:
        db_table (str): Nombre de la tabla en la base de datos a la cual este modelo corresponde.
    """
    idhotel = models.CharField(max_length=100, primary_key=True)
    nombreestablecimiento = models.CharField(max_length=100)

    horacheckin = models.TimeField()
    horacheckout = models.TimeField()
    petfriendly = models.CharField(max_length=2)
    servicio = models.CharField(max_length=100)
    numerointerior = models.CharField(max_length=100, blank=True, null=True)
    numeroexterior = models.IntegerField()
    colonia = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreestablecimiento

    class Meta:
        db_table = 'hotel'
