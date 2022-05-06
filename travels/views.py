from django.shortcuts import render, redirect

# from . import aco
from . import forms
from . import models

# Create your views here.
def createtravel(request):
    user = request.user
    if request.method == "POST":
        form = forms.CreateTravelForm(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            city = form.cleaned_data.get("city")  # 여행이름
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")
            lodging = form.cleaned_data.get("lodging")
            site = form.cleaned_data.get("site")
            count_date = (end_date - start_date).days
            new_travel = models.Travel.objects.create(
                name=city, start_date=start_date, end_date=end_date, user=user
            )
            new_lodging = models.Lodging.objects.create(
                travel=new_travel, name=lodging, latitude=0, longitude=2
            )
            new_place = models.Place.objects.create(
                travel=new_travel,
                name=site,
                day=count_date,
                order=1,
                latitude=0,
                longitude=2,
            )
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
    return render(request, "travels/checkpath.html", {"travel": travel})
