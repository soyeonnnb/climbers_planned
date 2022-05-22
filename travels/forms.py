from django import forms
from django.forms import modelformset_factory
from .models import Travel, Place, Lodging


class TravelModelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = (
            "name",
            "start_date",
            "end_date",
            "color",
            "latitude",
            "longitude",
        )
        labels = {
            "name": "여행지 name",
            "start_date": "여행지 start_date",
            "end_date": "여행지 end_date",
            "color": "여행지 color",
            "latitude": "여행지 위도",
            "longitude": "여행지 경도",
        }

        widgets = {
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "rows": 4, "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "rows": 4, "type": "date"}
            ),
            "color": forms.TextInput(attrs={"type": "color"}),
        }


class LodgingModelForm(forms.ModelForm):
    class Meta:
        model = Lodging
        fields = (
            "name",
            "latitude",
            "longitude",
        )
        labels = {
            "name": "숙소 name",
            "latitude": "숙소 위도",
            "longitude": "숙소 경도",
        }

PlaceFormset = modelformset_factory(
    Place, 
    fields=(
        "name",
        "latitude",
        "longitude",
    ), extra=1)