import random
from django.shortcuts import render, redirect

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
    place = models.Place.objects.filter(travel=pk).order_by("order")
    return render(request, "travels/checkpath.html", {"travel": travel, "place": place})
