from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from travels.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("core/", include("core.urls", namespace="core")),
    path("travels/", include("travels.urls", namespace="travels")),
    path('<int:id>', checkpath, name='checkpath'),
    path("users/", include("users.urls", namespace="users")),
    path('', main, name='core'), #?
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
