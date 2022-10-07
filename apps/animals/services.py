import random
from collections.abc import Iterator

from faker import Faker

from apps.animals import models
from apps.animals.typing import T_NAME

faker = Faker()


def generate_name(key: int | None = None) -> T_NAME:
    name = faker.first_name()
    if key:
        name = f"{name}_{random.randint(0, key)}"

    return name


def generate_animals(amount: int) -> Iterator[models.Animal]:
    names = set()

    while len(names) < amount:
        name = generate_name(key=amount)

        if name in names:
            continue

        names.add(name)
        yield models.Animal(
            name=name,
            age=random.randint(1, 15),
        )
