import random
from collections.abc import Iterator

from faker import Faker

from apps.humans.models import Human

faker = Faker()


def generate_human() -> Human:
    return Human(
        name=faker.unique.first_name(),
        age=random.randint(10, 100),
    )


def generate_humans(amount: int) -> Iterator[Human]:
    for _ in range(amount):
        yield generate_human()
