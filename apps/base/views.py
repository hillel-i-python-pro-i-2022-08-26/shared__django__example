from django.http import HttpRequest, HttpResponse

from apps.base.services.get_random_message import get_random_message


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(get_random_message())
