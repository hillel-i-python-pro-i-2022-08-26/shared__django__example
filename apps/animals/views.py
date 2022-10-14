from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AnimalForm
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


def edit_animal(request: HttpRequest, pk: int) -> HttpResponse:
    animal = Animal.objects.get(pk=pk)
    form = AnimalForm(instance=animal)

    return render(
        request,
        "animals/edit.html",
        {
            "form": form,
            "title": "Animals",
        },
    )
