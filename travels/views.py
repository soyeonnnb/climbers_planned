import random
from django.shortcuts import get_object_or_404, render, redirect
from . import forms
from . import models
from . import aco
from . import kmeans
from django.template import RequestContext

from django.contrib.auth.decorators import login_required


@login_required
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
                ### place fake data ###
                place.save()
            kmeans.kmeans_run(travel, count_date)
            aco.aco_run(travel, count_date, shell=False)
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


@login_required
def checkpath(request, pk):
    travel = models.Travel.objects.get(pk=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk).order_by("order"):
        places.append(p)
    # places = sorted(places, key=models.Place.day)
    count_date = (travel.end_date - travel.start_date).days + 1
    chk_day = [[] for _ in range(count_date)]
    for i in places:
        chk_day[i.day - 1].append(i)
    for i in range(len(chk_day)):
        chk_day[i].insert(0, i + 1)
    print(chk_day)
    return render(
        request,
        "travels/checkpath.html",
        {"travel": travel, "places": places, "chk_day": chk_day},
    )


@login_required
def savepath(request):  # 경로 저장
    # 경로 저장의 경우, 여행지 추가하는 과정에서 이미 db를 넘겨줌.
    return redirect("core")


@login_required
def checktravel(request, pk):
    travel = get_object_or_404(models.Travel, pk=pk)
    lodging = models.Lodging.objects.get(travel=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk):
        places.append(p)
    count_date = (travel.end_date - travel.start_date).days + 1
    chk_day = [[] for _ in range(count_date)]
    for i in places:
        chk_day[i.day - 1].append(i)
    for i in range(len(chk_day)):
        chk_day[i].insert(0, i + 1)

    # places = sorted(places, key=models.Place.day)
    return render(
        request,
        "travels/checktravel.html",
        {"travel": travel, "lodging": lodging, "places": places, "chk_day": chk_day},
    )


def deletetravel(request, pk):
    travel = get_object_or_404(models.Travel, pk=pk)
    lodging = models.Lodging.objects.get(travel=pk)
    places = []
    for p in models.Place.objects.filter(travel=pk):
        places.append(p)
    travel.delete()
    lodging.delete()
    for p in places:
        p.delete()
    return redirect("core")
