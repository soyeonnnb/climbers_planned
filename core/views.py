from django.shortcuts import render, get_object_or_404
from travels import models
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):
    user = request.user
    alltravel = models.Travel.objects.filter(user=user)
    return render(request, "core.html", {"alltravel": alltravel})
