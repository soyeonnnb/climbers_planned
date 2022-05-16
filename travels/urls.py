from django.urls import path
from travels.views import *

app_name = "travels"

urlpatterns = [
    path("<int:pk>/", checkpath, name="checkpath"),
    path("createtravel/", create_travel, name="createtravel"),
<<<<<<< HEAD
]
=======
]
>>>>>>> fea3ebf94ff72e4ae74d604adc691b7c48f8b73b
