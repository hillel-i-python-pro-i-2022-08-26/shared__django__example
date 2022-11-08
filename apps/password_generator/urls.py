from django.urls import path

from . import views

app_name = "password_generator"

urlpatterns = [
    path("<int:password_length>", views.GeneratePasswordView.as_view(), name="index"),
]
