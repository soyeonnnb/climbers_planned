from django.urls import path
from travels.views import *

app_name = "travels"

urlpatterns = [
    path("<int:pk>/", checkpath, name="checkpath"),
    path("createtravel/", create_travel, name="createtravel"),
    path("savepath/", savepath, name="savepath"),
    path("mytravel/<int:pk>/", checktravel, name='checktravel'),
    path('addplace/', addplace, name='addplace'),
]
