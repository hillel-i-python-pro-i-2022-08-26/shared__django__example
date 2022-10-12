# Register your models here.
from django.contrib import admin

from . import models

admin.site.register(models.Animal)


class AnimalInline(admin.TabularInline):
    model = models.Animal


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = (AnimalInline,)
