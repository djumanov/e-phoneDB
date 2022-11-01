from django.urls import path
from .views import (
    CompaniesView,
    ProductsView,
    CreateProductView,
    AddCompanyView,
    DeleteCompanyView,
    DeleteProductView,
    UpdateCompanyView,
    UpdateProductView,
    GetCompanyByIdView,
    GetProductByIdView,
    GetCompanyByNameView,
    GetProductByNameView,
    GetProductByColorView,
    GetProductByRamView,
)

urlpatterns = [
    path(route='companies/', view=CompaniesView.as_view(), name='companies'),
    path(route='company/<int:id>', view=GetCompanyByIdView.as_view(), name='get_company'),
    path(route='company/name/<str:name>', view=GetCompanyByNameView.as_view(), name='get_company_by_name'),
    path(route='add_company/', view=AddCompanyView.as_view(), name='add_company'),
    path(route='products/', view=ProductsView.as_view(), name='products'),
    path(route='product/<int:id>', view=GetProductByIdView.as_view(), name='get_product'),
    path(route='product/name/<str:name>', view=GetProductByNameView.as_view(), name='get_product_by_name'),
    path(route='product/color/<str:color>', view=GetProductByColorView.as_view(), name='get_product_by_color'),
    path(route='product/ram/<int:ram>', view=GetProductByRamView.as_view(), name='get_product_by_ram'),
    path(route='create_product/', view=CreateProductView.as_view(), name='create_product'),
    path(route='delete_company/<int:id>', view=DeleteCompanyView.as_view(), name='delete_company'),
    path(route='delete_product/<int:id>', view=DeleteProductView.as_view(), name='delete_product'),
    path(route='update_company/<int:id>', view=UpdateCompanyView.as_view(), name='update_company'),
    path(route='update_product/<int:id>', view=UpdateProductView.as_view(), name='update_product'),
]