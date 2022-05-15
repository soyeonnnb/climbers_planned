import random
from django.shortcuts import render, redirect

from . import aco

from . import forms
from . import models

# Create your views here.


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
            lodging = lodgingform.save(commit=False)
            lodging.travel = travel
            ### lodging fake data###
            lodging.latitude = 1
            lodging.longitude = 1
            lodging.save()
            ### lodging fake data###
            for form in placeformset:
                place = form.save(commit=False)
                place_cd = form.cleaned_data
                place_name = place_cd.get("name")
                if place_name == None:
                    continue
                place.travel = travel
                ### place fake data ###
                place.day = 1
                place.order = 1
                place.latitude = 1
                place.longitude = 1
                ### place fake data ###
                place.save()
            return redirect("travels:checkpath", pk=travel.pk)
    else:
        travelform = forms.TravelModelForm(request.GET or None, prefix="travel")
        lodgingform = forms.LodgingModelForm(request.GET or None, prefix="lodging")
        placeformset = forms.PlaceFormset(
            queryset=models.Place.objects.none(), prefix="places"
        )
    return render(
        request,
        "travels/createtravel_test.html",
        {
            "travelform": travelform,
            "lodgingform": lodgingform,
            "placeformset": placeformset,
        },
    )


def createtravel(request):
    user = request.user
    if request.method == "POST":
        form = forms.CreateTravelForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            city = form.cleaned_data.get("city")  # 여행이름
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            lodging = form.cleaned_data.get("lodging")
            count_date = (end_date - start_date).days + 1
            new_travel = models.Travel.objects.create(
                name=city, start_date=start_date, end_date=end_date, user=user
            )
            for i in range(1, 6):
                site_name = "site-" + str(i)
                site = form.cleaned_data.get(site_name)
                models.Place.objects.create(
                    travel=new_travel,
                    name=site,
                    day=1,
                    order=1,
                    latitude=1,
                    longitude=1,
                )
            # new_place.save()
            # new_place = models.Place.objects.create(
            #     travel=new_travel,
            #     name=site, day=day, order=order
            # )

            # 여기부터 aco.aco_run 까지는 소연님 aco 코드
            # new_lodging = models.Lodging.objects.create(
            #     travel=new_travel,
            #     name=lodging,
            #     latitude=random.uniform(0, 5),
            #     longitude=random.uniform(0, 5),
            # )
            # for i in range(10):
            #     new_place = models.Place.objects.create(
            #         travel=new_travel,
            #         name=site + str(i),
            #         day=random.randint(1, count_date),
            #         order=0,
            #         latitude=random.uniform(0, 5),
            #         longitude=random.uniform(0, 5),
            #     )
            #     new_place.save()
            # aco.aco_run(new_travel, count_date)
            return redirect("travels:checkpath", pk=new_travel.pk)
    else:
        form = forms.CreateTravelForm()
    return render(
        request,
        "travels/createtravel.html",
        {
            "form": form,
        },
    )


def checkpath(request, pk):
    travel = models.Travel.objects.get(pk=pk)
    place = models.Place.objects.filter(travel=pk).order_by("order")
    return render(request, "travels/checkpath.html", {"travel": travel, "place": place})
