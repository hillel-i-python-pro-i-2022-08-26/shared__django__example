from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.humans.services import generate_humans


def get_humans(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "humans/index.html",
        {
            "humans": generate_humans(amount=10),
            "title": "Humans",
        },
    )
