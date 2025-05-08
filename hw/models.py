import datetime

from django.db import models


class ListHeadTable(models.Model):
    """
    Списки колонок в таблиці
    """
    name = models.CharField(
        verbose_name="Назва",
        max_length=10,
        default="test"
    )
    names = models.JSONField(
        verbose_name="Список колонок в таблиці",
    )
    date_update = models.DateField(
        verbose_name="Дата оновлення запису",
        auto_now=True,
    )
    time_update = models.TimeField(
        verbose_name="Час оновлення запису",
        auto_now=True
    )

    # def save(self, *args, **kwargs):
    #     self.date_update = datetime.date.today()
    #     self.time_update = datetime.datetime.now().time()

    class Meta:
        verbose_name = "Колонки"
        verbose_name_plural = "Колонки"


class Howitzers(models.Model):
    """
    Гармати
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Модель гармати",
        unique=True,
    )
    caliber = models.CharField(
        max_length=50,
        verbose_name="Калібр гармати",
    )
    projectiles = models.JSONField(
        verbose_name="Типи снарядів",
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Гармата"
        verbose_name_plural = "Гармати"


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
    to_howitzer = models.ForeignKey(
        to=Howitzers,
        verbose_name="",
        on_delete=models.SET_NULL,
        related_name="position_howitzer",
        blank=True, null=True,
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вогнева позиція"
        verbose_name_plural = "Вогневі позиції"


class Target(models.Model):
    """
    Ціль стрільби
    """
    name = models.CharField(
        verbose_name="Назва цілі",
        max_length=150,
    )
    square = models.CharField(
        max_length=6,
        verbose_name="Квадрат",
    )
    coordinate_x = models.CharField(
        verbose_name="Координата X",
        max_length=10,
    )
    coordinate_y = models.CharField(
        verbose_name="Координата Y",
        max_length=10,
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ціль"
        verbose_name_plural = "Цілі"


class CharacterTarget(models.Model):
    """
    Характер цілі
    """
    name = models.CharField(
        verbose_name="Характер цілі",
        max_length=200,
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характер цілі"
        verbose_name_plural = "Характери цілей"


class ResultShooting(models.Model):
    """
    Результат стрільби
    """
    name = models.CharField(
        verbose_name="Результат стрільби",
        max_length=200,
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Результат стрільби"
        verbose_name_plural = "Результати стрільб"


class Shoot(models.Model):
    """
    Стрільба
    """

    class PhotoVideoChoices(models.TextChoices):
        YES = "Так"
        NO = "Ні"
        UNK = "???"

    date_begin = models.DateField(
        verbose_name="Дата початку",
    )
    time_begin = models.TimeField(
        verbose_name="Час початку",
    )
    time_end = models.TimeField(
        verbose_name="Час завершення",
    )
    get_from = models.CharField(
        verbose_name="",
        max_length=100,
        default="Розвідка1БрОП",
    )
    to_position = models.ForeignKey(
        to=Position,
        verbose_name="Вогнева позиція",
        on_delete=models.SET_NULL,
        related_name="shoot_position",
        blank=True, null=True,
    )
    count_shoot = models.PositiveSmallIntegerField(
        verbose_name="К-ть пострілів",
        default=0,
    )
    to_target = models.ForeignKey(
        to=Target,
        verbose_name="Ціль",
        on_delete=models.SET_NULL,
        related_name="shoot_target",
        blank=True, null=True,
    )
    to_character = models.ForeignKey(
        to=CharacterTarget,
        verbose_name="Характер цілі",
        on_delete=models.SET_NULL,
        related_name="shoot_character",
        blank=True, null=True,
    )
    to_result = models.ForeignKey(
        to=ResultShooting,
        verbose_name="",
        on_delete=models.SET_NULL,
        related_name="shoot_result",
        blank=True, null=True,
    )
    photo_video_check = models.CharField(
        verbose_name="Фото/Відео",
        choices=PhotoVideoChoices.choices,
        default=PhotoVideoChoices.UNK,
    )
    date_create = models.DateField(
        verbose_name="Дата створення запису",
        auto_now_add=True,
    )
    time_create = models.TimeField(
        verbose_name="Час створення запису",
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Стрільба"
        verbose_name_plural = "Стрільби"
