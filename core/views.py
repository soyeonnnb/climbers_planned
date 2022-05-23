from django.shortcuts import render, get_object_or_404
from travels import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):
    alltravel = models.Travel.objects.all()
    return render(request, "core.html", {"alltravel": alltravel})

