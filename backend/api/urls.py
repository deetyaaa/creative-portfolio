from django.urls import path
from .views import CreatorListCreate

urlpatterns = [
    path("creators/", CreatorListCreate.as_view(), name="creators"),
]