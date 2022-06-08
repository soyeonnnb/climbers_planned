from django.urls import path
from travels.views import *

app_name = "travels"

urlpatterns = [
    path("<int:pk>/", checkpath, name="checkpath"),
    path("createtravel/", create_travel, name="createtravel"),
    path("checktravel/<int:pk>/", checktravel, name="checktravel"),
    path("deletetravel/<int:pk>/", deletetravel, name="deletetravel"),
]
