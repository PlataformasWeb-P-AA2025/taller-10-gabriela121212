from django.db import models

# Create your models here.
class Parroquia(models.Model):
    UBICACION = [
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste')
    ]

    TIPO = [
        ('urbana', 'Urbana'),
        ('rural', 'Rural')
    ]

    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=10, choices=UBICACION)
    tipo = models.CharField(max_length=10, choices=TIPO)

    def __str__(self):
        return "%d) %s [%s - %s]" % (
            self.id, self.nombre,
            self.ubicacion,
            self.tipo
        )

class Barrio(models.Model):
    NUM_PARQUES = [(i, str(i)) for i in range(1, 7)]

    nombre = models.CharField(max_length=100)
    numero_viviendas = models.PositiveIntegerField()
    numero_parques = models.IntegerField(choices=NUM_PARQUES)
    numeroE_residenciales = models.PositiveIntegerField()
    
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name="mis_barrios")

    def __str__(self):
        return "%s - Viviendas: %d - Parques: %d - Edificios: %d" % (
            self.nombre,
            self.numero_viviendas,
            self.numero_parques,
            self.numeroE_residenciales
        )
