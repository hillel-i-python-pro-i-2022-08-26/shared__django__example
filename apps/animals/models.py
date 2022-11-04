import uuid

from django.db import models
from django.urls import reverse

from apps.animals.typing import T_NAME


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


def get_icon_path(instance, filename: str) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"animals/animal/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Animal(models.Model):
    name: T_NAME = models.CharField(max_length=100)

    age = models.PositiveSmallIntegerField()

    date = models.DateField(null=True, blank=True, default=None)

    is_auto_generated = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    group = models.ForeignKey(
        Group,
        related_name="animals",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("animals:edit", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__
