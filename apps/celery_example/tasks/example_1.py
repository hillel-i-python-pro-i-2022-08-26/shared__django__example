import logging
import random
import uuid
from time import sleep

from celery import shared_task


# from apps.animals.models import Animal

# T_ANIMAL_ID: TypeAlias = int


# def example_1(animal_id: T_ANIMAL_ID):


@shared_task
def example_1(value: str):
    logger = logging.getLogger("django")

    # animal = Animal.objects.get(id=animal_id)

    id_ = uuid.uuid4()

    logger.info(f"[{id_}] example_1: {value}")
    wait_for = random.randint(1, 10)
    logger.info(f"[{id_}] example_1: wait_for: {wait_for}")
    sleep(wait_for)
    logger.info(f"[{id_}] example_1: completed")

    return
