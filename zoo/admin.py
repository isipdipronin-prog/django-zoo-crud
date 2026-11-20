from django.contrib import admin
from .models import (
    AnimalClass, Habitat, Diet, Enclosure,
    Keeper, Animal, VetCard, FeedingSchedule
)


@admin.register(AnimalClass)
class AnimalClassAdmin(admin.ModelAdmin):
    pass


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    pass


@admin.register(Diet)
class DietAdmin(admin.ModelAdmin):
    pass


@admin.register(Enclosure)
class EnclosureAdmin(admin.ModelAdmin):
    pass


@admin.register(Keeper)
class KeeperAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(VetCard)
class VetCardAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedingSchedule)
class FeedingScheduleAdmin(admin.ModelAdmin):
    pass