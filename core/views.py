from django.shortcuts import render, get_object_or_404
from travels import models

# Create your views here.
def main(request):
    alltravel = models.Travel.objects.all()
    return render(request, "core.html", {"alltravel": alltravel})
