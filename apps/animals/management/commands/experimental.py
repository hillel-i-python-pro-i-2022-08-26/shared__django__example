import logging

from django.core.management import BaseCommand

from apps.animals import models


class Command(BaseCommand):
    help = "Experimental"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger("django")

    def handle(self, *args, **options):
        self.logger.info("Experimental")
        group = models.Group.objects.first()

        related_animals = group.animals.all()
