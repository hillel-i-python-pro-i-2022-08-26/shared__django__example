from django.urls import path

from . import views

app_name = "celery_example"

urlpatterns = [
    path("", views.CeleryView.as_view(), name="index"),
]
