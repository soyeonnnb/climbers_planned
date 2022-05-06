from django.urls import path
from travels.views import *

app_name = "travels"

urlpatterns = [
    path("<int:pk>/", checkpath, name="checkpath"),
    path("createtravel/", createtravel, name="createtravel"),
]
