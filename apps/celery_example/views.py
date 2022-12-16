from celery.result import AsyncResult
from django.views.generic import TemplateView

from apps.celery_example.tasks import example_1


class CeleryView(TemplateView):
    template_name = "celery_example/index.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        result: AsyncResult = example_1.delay("Hello, world!")

        context_data["result_id"] = result.id

        return context_data
