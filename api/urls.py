from os import name
from django.urls import path
from .views import (
    CompaniesView,
)

urlpatterns = [
    path(route='companies/', view=CompaniesView.as_view(), name='companies'),
]