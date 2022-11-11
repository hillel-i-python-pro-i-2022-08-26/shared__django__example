import logging
from collections.abc import Callable
from typing import ClassVar

from django.http import HttpRequest


class SimpleLoggingMiddleware:
    _NAME: ClassVar[str] = "first"

    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.logger = logging.getLogger("django")
        self.logger.info(f"Init {self._NAME}")

    def __call__(self, request: HttpRequest):
        session = request.session

        if not session.session_key:
            session.save()

        session_key = session.session_key

        message = f"[{self._NAME}] {request.path} {request.user.is_authenticated} {request.user} {session_key}"

        self.logger.info(f"[before] {message}")
        response = self.get_response(request)
        self.logger.info(f"[after] {message}")
        return response


class SimpleLoggingMiddleware2(SimpleLoggingMiddleware):
    _NAME: ClassVar[str] = "second"
