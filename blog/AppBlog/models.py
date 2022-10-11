from django.db import models

# Create your models here.


class Equipo(models.Model):
    name = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    foundation_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Jugador(models.Model):
    class Meta:
        verbose_name_plural = "Jugadores"

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    birth = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Entrenador(models.Model):
    class Meta:
        verbose_name_plural = "Entrenadores"

    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    birth = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
