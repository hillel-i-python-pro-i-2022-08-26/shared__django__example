from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from webargs import fields
from webargs.djangoparser import use_args

from apps.humans.services import generate_humans


@use_args({"amount": fields.Int(missing=10)}, location="query")
def get_humans(request: HttpRequest, args) -> HttpResponse:
    amount = args["amount"]

    return render(
        request,
        "humans/index.html",
        {
            "humans": generate_humans(amount=amount),
            "title": "Humans",
        },
    )
