from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView

from .models import Animal


class ArticleListView(ListView):
    model = Animal


@method_decorator(login_required, name="post")
class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "id",
        "name",
        "age",
        "avatar",
    )
    template_name_suffix = "_update_form"
