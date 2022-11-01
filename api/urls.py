from django.urls import path
from .views import (
    CompaniesView,
    ProductsView,
    CreateProductView,
    AddCompanyView,
)

urlpatterns = [
    path(route='companies/', view=CompaniesView.as_view(), name='companies'),
    path(route='add_company/', view=AddCompanyView.as_view(), name='add_company'),
    path(route='products/', view=ProductsView.as_view(), name='products'),
    path(route='create_product/', view=CreateProductView.as_view(), name='create_product'),
]