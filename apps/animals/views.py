from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView, CreateView

from .models import Animal


class ArticleListView(ListView):
    model = Animal


class AnimalCreateView(CreateView):
    model = Animal
    fields = (
        "name",
        "age",
        "avatar",
    )

    success_url = reverse_lazy("animals:index")


@method_decorator(login_required, name="post")
class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "id",
        "name",
        "age",
        "avatar",
    )

    success_url = reverse_lazy("animals:index")
