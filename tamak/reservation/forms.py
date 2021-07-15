from django import forms
from django.db.models.enums import IntegerChoices
from django.forms import widgets
from django.forms.widgets import DateInput, NumberInput, Textarea, TimeInput
from .models import ReservationCreate


class ReservationCreateForm(forms.ModelForm):
    class Meta:
        model = ReservationCreate
        exclude = ['client']

        widgets = {
            "date_of_reservation": forms.DateInput(
                attrs={
                    "class": "form-control datetimepicker-input",
                    "data-target": "#datetimepicker4",
                    "placeholder": "Date",
                    "type": "date",
                }
            ),
            "time_of_reservation": forms.TimeInput(
                attrs={
                    "class": "form-control timepicker-input",
                    "data-target": "#datetimepicker3",
                    "placeholder": "Time",
                    "type": "time",
                }
            ),
            "persons": forms.Select(
                attrs={"class": "form-control", "id": "selectPerson"}
            ),
            "comment": forms.Textarea(attrs={"cols": 30, "rows": 3}),
            "number_of_phone": forms.NumberInput(
                attrs={
                    "class": "form-control number-input",
                    "placeholder": "550123456",
                    "type": "number",
                }
            ),
        }