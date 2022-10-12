from django.urls import path

from . import views

app_name = "session_example"

urlpatterns = [
    path("", views.session_example_view, name="index"),
]
