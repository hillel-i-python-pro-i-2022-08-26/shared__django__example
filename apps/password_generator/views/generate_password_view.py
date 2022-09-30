from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.password_generator.services.generate_password import generate_password


def generate_password_view(request: HttpRequest, password_length: int) -> HttpResponse:
    return render(
        request,
        "password_generator/index.html",
        {
            "password": generate_password(password_length=password_length),
        },
    )
