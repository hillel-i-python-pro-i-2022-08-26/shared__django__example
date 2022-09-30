from typing import NamedTuple


class Human(NamedTuple):
    name: str
    age: int

    def __str__(self):
        return f"{self.name}: {self.age}"

    # __repr__ = __str__
