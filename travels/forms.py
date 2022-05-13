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
            "name": "여행지name",
            "start_date": "여행지start_date",
            "end_date": "여행지end_date",
            "color": "여행지color",
        }


class LodgingModelForm(forms.ModelForm):
    class Meta:
        model = Lodging
        fields = ("name",)
        labels = {
            "name": "숙소name",
        }


PlaceFormset = modelformset_factory(
    Place,
    fields=("name",),
    extra=1,
)


class CreateTravelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        site = []
        sites = Place.objects.all()
        super(CreateTravelForm, self).__init__(*args, **kwargs)
        counter = 1
        # for s in sites:
        for s in range(5):  # 여행장소 5개로 임의지정
            self.fields["site-" + str(counter)] = forms.CharField(label="site")
            counter += 1

    city = forms.CharField()  # 여행이름
    start_date = forms.DateField()
    end_date = forms.DateField()
    lodging = forms.CharField()
