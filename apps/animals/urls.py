from django.urls import path

from . import views

app_name = "animals"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="index"),
    # path("<int:pk>", views.edit_animal, name="edit"),
    path("create", views.AnimalCreateView.as_view(), name="create"),
    path("<int:pk>", views.AnimalUpdateView.as_view(), name="edit"),
]
