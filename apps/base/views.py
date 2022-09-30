from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from apps.base.services.get_random_message import get_random_message


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "index.html",
        {
            "random_message": get_random_message(),
        },
    )
