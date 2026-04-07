from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("pl/", views.pl_endpoint),
    path("pdp/", views.pdp_endpoint),
]