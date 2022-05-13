from django import forms
from .models import Travel, Place, Lodging


class CreateTravelForm(forms.Form):
    def __init__(self, *args, **kwargs):
        site = []
        sites = Place.objects.all()
        super(CreateTravelForm, self).__init__(*args, **kwargs)
        counter = 1
        # for s in sites:
        for s in range(5): #여행장소 5개로 임의지정
            self.fields['site-' + str(counter)] = forms.CharField(label='site')
            counter += 1
    city = forms.CharField() #여행이름
    start_date = forms.DateField()
    end_date = forms.DateField()
    lodging = forms.CharField()
    # site = forms.CharField() #여행지 추가
    
    # class Meta:
    #     model = Travel
    #     fields = ['name', 'start_date', 'end_date']


# class PlaceForm(forms.Form):
#     name = forms.CharField(
#         label = ''
#     )

# class PlaceForm(forms.ModelForm):
#     class Meta:
#         model = Place
#         fields = ['name']

# class LodgingForm(forms.ModelForm):
#     class Meta:
#         model = Lodging
#         fields = ['name']
