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
        )
        labels = {
            "name": "여행지 name",
            "start_date": "여행지 start_date",
            "end_date": "여행지 end_date",
            "color": "여행지 color",
        }


class LodgingModelForm(forms.ModelForm):
    class Meta:
        model = Lodging
        fields = ("name",)
        labels = {
            "name": "숙소 name",
        }

PlaceFormset = modelformset_factory(Place, fields=("name",), extra=1)
<<<<<<< HEAD

=======
>>>>>>> 5c8888e540f4bc6a57dac0d022cc65c5b2d6c9d3
