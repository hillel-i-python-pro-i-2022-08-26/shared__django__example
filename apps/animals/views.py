from django.views.generic import UpdateView, ListView

from .models import Animal


class ArticleListView(ListView):
    model = Animal


class AnimalUpdateView(UpdateView):
    model = Animal
    fields = (
        "id",
        "name",
        "age",
        "avatar",
    )
    template_name_suffix = "_update_form"
