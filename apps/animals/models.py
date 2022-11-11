import base64
import uuid

from django.db import models
from django.urls import reverse

from apps.animals.typing import T_NAME


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


def _generate_pseudo_id(amount_of_iterations: int = 3) -> str:
    # [validate]-[BEGIN]
    if amount_of_iterations <= 0:
        raise ValueError(f'Please provide positive amount of iterations. Current: "{amount_of_iterations}"')
    # [validate]-[END]

    return (
        base64.urlsafe_b64encode(b"".join(uuid.uuid4().bytes for _ in range(amount_of_iterations)))
        .decode()
        .replace("=", "")
    )


# noinspection PyUnusedLocal
def get_icon_path(
    instance,
    filename: str,
) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)

    return (
        f"animals/animal/avatar/"
        f"{_generate_pseudo_id(amount_of_iterations=1)}/"
        f"{_generate_pseudo_id(amount_of_iterations=5)}/"
        f"avatar.{extension}"
    )


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
