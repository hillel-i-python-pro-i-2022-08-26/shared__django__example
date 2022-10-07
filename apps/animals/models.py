from django.db import models

from apps.animals.typing import T_NAME


# class Group(models.Model):
#     name = models.CharField(max_length=100)


class Animal(models.Model):
    name: T_NAME = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    is_auto_generated = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # group = models.ForeignKey(Group, related_name='animals', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__
