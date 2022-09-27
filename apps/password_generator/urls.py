from django.urls import path

from . import views

urlpatterns = [path("<int:password_length>", views.generate_password_view, name="index")]
