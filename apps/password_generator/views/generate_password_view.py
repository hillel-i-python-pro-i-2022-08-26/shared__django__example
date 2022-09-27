from django.http import HttpRequest, HttpResponse

from apps.password_generator.services.generate_password import generate_password


def generate_password_view(request: HttpRequest, password_length: int) -> HttpResponse:
    return HttpResponse(generate_password(password_length=password_length))
