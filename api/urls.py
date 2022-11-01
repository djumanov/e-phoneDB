from django.urls import path
from .views import (
    CompaniesView,
    ProductsView,
    CreateProductView,
    AddCompanyView,
    DeleteCompanyView,
    DeleteProductView,
    GetCompanyByIdView,
    GetProductByIdView,
)

urlpatterns = [
    path(route='companies/', view=CompaniesView.as_view(), name='companies'),
    path(route='company/<int:id>', view=GetCompanyByIdView.as_view(), name='get_company'),
    path(route='add_company/', view=AddCompanyView.as_view(), name='add_company'),
    path(route='products/', view=ProductsView.as_view(), name='products'),
    path(route='product/<int:id>', view=GetProductByIdView.as_view(), name='get_product'),
    path(route='create_product/', view=CreateProductView.as_view(), name='create_product'),
    path(route='delete_company/<int:id>', view=DeleteCompanyView.as_view(), name='delete_company'),
    path(route='delete_product/<int:id>', view=DeleteProductView.as_view(), name='delete_product'),
]