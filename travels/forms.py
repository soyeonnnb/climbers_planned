from django import forms
from .models import Travel, Place, Lodging


class CreateTravelForm(forms.Form):
    city = forms.CharField()  # 여행이름
    start_date = forms.DateField()
    end_date = forms.DateField()
    lodging = forms.CharField()
    site = forms.CharField()  # 여행지 추가
