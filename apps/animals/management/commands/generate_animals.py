import logging

from django.core.management import BaseCommand, CommandParser

from apps.animals import models
from apps.animals.services import generate_animals


class Command(BaseCommand):
    help = "Generate required amount of animals"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            "--amount",
            type=int,
            default=10,
            help="Amount of generated animals",
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]
        self.logger.info(f"Generate {amount} animals")

        current_amount = models.Animal.objects.all().count()
        self.logger.info(f"Current amount of animals: {current_amount}")

        for number, animal in enumerate(generate_animals(amount=amount), start=1):
            message = f"Generating animal. {number}/{amount}."
            self.logger.info(f"{message} Start")
            animal.is_auto_generated = True
            animal.save()
            self.logger.info(f"{message} End")

        amount_after_generating = models.Animal.objects.all().count()
        self.logger.info(f"Amount of animals after generating: {amount_after_generating}")
