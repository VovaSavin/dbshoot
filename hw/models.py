from django.db import models


class Howitzers(models.Model):
    """
    Гармати
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Модель гармати",
    )
    caliber = models.CharField(
        max_length=50,
        verbose_name="Калібр гармати",
    )
    projectiles = models.JSONField(
        verbose_name="Типи снарядів",
    )


# Create your models here.
class Position(models.Model):
    """
    ВПшка
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Вогнева позиція",
    )
    remainder = models.SmallIntegerField(
        verbose_name="Залишок снарядів",
    )
