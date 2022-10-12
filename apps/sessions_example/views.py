from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

KEY__COUNT_OF_VISITS = "count_of_visits"


def session_example_view(request: HttpRequest) -> HttpResponse:
    session = request.session
    count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)

    count_of_visits += 1

    session[KEY__COUNT_OF_VISITS] = count_of_visits

    return render(
        request,
        "session_example/index.html",
        {
            "session_id": session.session_key,
            "count_of_visits": count_of_visits,
            "title": "Session example",
        },
    )
