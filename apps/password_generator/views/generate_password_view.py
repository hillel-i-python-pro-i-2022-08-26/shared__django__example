from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from apps.password_generator.services.generate_password import generate_password


@method_decorator(login_required, name="get")
class GeneratePasswordView(TemplateView):
    template_name = "password_generator/index.html"

    def get_context_data(self, password_length: int, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["password"] = generate_password(password_length=password_length)

        return context_data
