from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Company, Product
import json


def convert_to_dict(product: Product) -> dict:
    company: Company = Company.objects.get(id=product.company_id)
    product_dict = {
        'id': product.id,
        'name': product.name,
        'color': product.color,
        'ram': product.ram,
        'memory': product.memory,
        'price': product.price,
        'image': product.image,
        'released_date': product.released_date,
        'created_at': product.created_at,
        'updated_at': product.updated_at,
        'company': company.name
    }

    return product_dict



class CompaniesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        companies = Company.objects.all()
        companies_json = dict()
        for company in companies: 
            companies_json[company.name] = {
                'id': company.id,
                'logo': company.logo,
                'description': company.description,
                'website': company.website,
            }

        return JsonResponse(data=companies_json)


class ProductsView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.all()
        products_json = {'products': []}
        for product in products:
            products_json['products'].append(convert_to_dict(product))

        return JsonResponse(data=products_json)

