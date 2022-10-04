from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"

    __repr__ = __str__
