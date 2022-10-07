from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Animal


def get_animals(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()

    return render(
        request,
        "animals/index.html",
        {
            "animals": animals,
            "title": "Animals",
        },
    )
