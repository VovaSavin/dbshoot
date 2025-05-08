from django.contrib import admin
from .models import (
    ListHeadTable,
    Howitzers,
    Position,
    Target,
    CharacterTarget,
    ResultShooting,
    Shoot,
)


# Register your models here.

@admin.register(ListHeadTable)
class ListHeadTableAdmin(admin.ModelAdmin):
    list_display = [
        "names", "id",
    ]


@admin.register(Howitzers)
class HowitzersAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "caliber",
        "date_create",
        "id",
    ]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "to_howitzer",
        "remainder",
        "date_create",
        "id",
    ]


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "square",
        "coordinate_x",
        "coordinate_y",
        "date_create",
        "id",
    ]


@admin.register(CharacterTarget)
class CharacterTargetAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date_create",
        "id",
    ]


@admin.register(ResultShooting)
class ResultShootingAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date_create",
        "id",
    ]


@admin.register(Shoot)
class ShootAdmin(admin.ModelAdmin):
    list_display = [
        "date_begin",
        "time_begin",
        "time_end",
        "to_position",
        "to_target",
        "to_character",
        "to_result",
        "id",
    ]
