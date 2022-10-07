from django.urls import path

from . import views

app_name = "animals"

urlpatterns = [
    path("", views.get_animals, name="index"),
]
