from django.urls import path
from .views import (
    CompaniesView,
    ProductsView,
)

urlpatterns = [
    path(route='companies/', view=CompaniesView.as_view(), name='companies'),
    path(route='products/', view=ProductsView.as_view(), name='products'),
]