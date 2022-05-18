import random
from unicodedata import name 
from django.shortcuts import get_object_or_404, render, redirect
from . import forms
from . import models
from . import aco

def create_travel(request):
    user = request.user
    if request.method == "POST":
        travelform = forms.TravelModelForm(request.POST, prefix="travel")
        lodgingform = forms.LodgingModelForm(request.POST, prefix="lodging")
        placeformset = forms.PlaceFormset(request.POST, prefix="places")
        if travelform.is_valid() and lodgingform.is_valid() and placeformset.is_valid():
            travel = travelform.save(commit=False)
            travel.user = user
            travel.save()
            start_date = travelform.cleaned_data.get("start_date")
            end_date = travelform.cleaned_data.get("end_date")
            count_date = (end_date - start_date).days + 1
            lodging = lodgingform.save(commit=False)
            lodging.travel = travel
            ### lodging fake data###
            lodging.latitude = random.uniform(0, 5)
            lodging.longitude = random.uniform(0, 5)
            lodging.save()
            ### lodging fake data###
            for form in placeformset:
                place = form.save(commit=False)
                place_name = form.cleaned_data.get("name")
                if place_name == None:
                    continue
                place.travel = travel
                place.order = 0  # order이 null이 되면 안되서 0으로 채워줌
                ### place fake data ###
                place.day = random.randint(1, count_date)
                place.latitude = random.uniform(0, 5)
                place.longitude = random.uniform(0, 5)
                ### place fake data ###
                place.save()
            aco.aco_run(travel, count_date)
            return redirect("travels:checkpath", pk=travel.pk)
    else:
        travelform = forms.TravelModelForm(request.GET or None, prefix="travel")
        lodgingform = forms.LodgingModelForm(request.GET or None, prefix="lodging")
        placeformset = forms.PlaceFormset(
            queryset=models.Place.objects.none(), prefix="places"
        )
    return render(
        request,
        "travels/createtravel.html",
        {
            "travelform": travelform,
            "lodgingform": lodgingform,
            "placeformset": placeformset,
        },
    )


def checkpath(request, pk):
    travel = models.Travel.objects.get(pk=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk).order_by('order'):
        places.append(p)
    # places = sorted(places, key=models.Place.day)
    return render(request, "travels/checkpath.html", {"travel": travel, "places":places})

def savepath(request): #경로 저장
    # 경로 저장의 경우, 여행지 추가하는 과정에서 이미 db를 넘겨주므로 db에 저장할 필요 없는 것 같은데.. 맞나요?
    # 시퀀스 다이어그램 상 다시 저장해주어야 하긴 하는데.. 갱신 아닌지.. 근데 갱신할 필요가 없는 것 같아서요
    # travel = models.Travel.objects.get(pk=pk)
    # place = models.Place.objects.filter(travel=pk).order_by('order')
    # #db 저장 안 해도 되나?
    return redirect('core')

def checktravel(request, pk): 
    travel = get_object_or_404(models.Travel, pk=pk)
    lodging = models.Lodging.objects.get(travel=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk):
        places.append(p)
    # places = sorted(places, key=models.Place.day)
    return render(request, 'travels/checktravel.html', {'travel':travel, 'lodging':lodging, 'places':places})


def updatetravel(request, pk):
    travel = get_object_or_404(models.Travel, pk=pk)
    lodging = models.Lodging.objects.get(travel=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk):
        places.append(p)
    if request.method == "POST":
        travelform = forms.TravelModelForm(request.POST, prefix="travel")
        lodgingform = forms.LodgingModelForm(request.POST, prefix="lodging")
        placeformset = forms.PlaceFormset(request.POST, prefix="places")
        if not travel:
            return redirect("core")
        if travelform.is_valid() and lodgingform.is_valid() and placeformset.is_valid():
            travel_name = travelform.cleaned_data["travel_name"]
            travel_start_date = travelform.cleaned_data["travel_start_date"]
            travel_end_date = travelform.cleaned_data["travel_end_date"]
            lodging_name = lodgingform.cleaned_data["lodging_name"]
    
            travel.name = travel_name
            travel.start_date = travel_start_date
            travel.end_date = travel_end_date
            lodging.name = lodging_name

            for place in places:
                place_name = placeformset.cleaned_data["place_name"]
                place.name = place_name
                
            travel.save()
            lodging.save()
            places.save()
        return redirect("travels:checktravel", kwargs={"pk": pk})

    else:
        travel_form = forms.TravelModelForm(instance=travel)
        lodging_form = forms.LodgingModelForm(instance=lodging)
        placeformset = forms.PlaceFormset(instance=places)
    
    return render(
        request,
        "travels/updatetravel.html",
        {"travel_form": travel_form, "lodging_form": lodging_form, "placeformset": placeformset},
    )

# def updatetravel(request, pk):
#     travel = get_object_or_404(models.Travel, pk=pk)
#     lodging = models.Lodging.objects.get(travel=pk)
#     places = []
#     for p in models.Place.objects.filter(travel=pk):
#         places.append(p)
#     if request.method == "POST": #update
#         travel.name = request.POST.get("name", False)
#         lodging.name = request.POST.get("name", False)
#         travel.start_date = request.POST.get("start_date", False)
#         travel.end_date = request.POST.get("end_date", False)
#         for place in places:
#             place.name = request.POST.get("name", False)
#         # travel.save()
#         # lodging.save()
#         # places.save()
#         return redirect('travels:checktravel', pk=travel.pk)
#     return render(request, 'travels/updatetravel.html', {'travel':travel, 'lodging':lodging, 'places':places})