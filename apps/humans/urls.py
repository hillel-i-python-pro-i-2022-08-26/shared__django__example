from django.urls import path

from . import views

app_name = "humans"

urlpatterns = [
    path("", views.get_humans, name="index"),
]
