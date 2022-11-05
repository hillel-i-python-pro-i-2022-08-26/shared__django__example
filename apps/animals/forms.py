from django import forms
from django.forms import SelectDateWidget

from apps.animals.models import Animal


class AnimalForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Animal
        fields = (
            "name",
            "avatar",
            "age",
        )
