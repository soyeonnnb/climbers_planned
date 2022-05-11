from django import forms
from .models import Travel, Place, Lodging

class CreateTravelForm(forms.Form):
    city = forms.CharField() #여행이름
    start_date = forms.DateField()
    end_date = forms.DateField()
    lodging = forms.CharField()
    site = forms.CharField() #여행지 추가

    # class Meta:
    #     model = Travel
    #     fields = ['name', 'start_date', 'end_date']

# class PlaceForm(forms.ModelForm):
#     class Meta:
#         model = Place
#         fields = ['name']

# class LodgingForm(forms.ModelForm):
#     class Meta:
#         model = Lodging
#         fields = ['name']
