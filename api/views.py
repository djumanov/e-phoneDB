from datetime import date
from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Company, Product
import json
from datetime import date, datetime
from django.db.models import Q


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


class AddCompanyView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        data = request.POST
        Company.objects.create(
            name        = data.get('name'),
            logo        = data.get('logo'),
            description = data.get('description'),
            website     = data.get('website'),
        )
        
        return JsonResponse({'added_company': data})



class ProductsView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.all()
        products_json = {'products': []}
        for product in products:
            products_json['products'].append(convert_to_dict(product))

        return JsonResponse(data=products_json)


class CreateProductView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        # try:
        data = request.POST
        company: Company = Company.objects.get(Q(name=data.get('company')))
        released_date_str = data.get('released_date')
        released_year, released_month, released_day = str(released_date_str).split('-')
        Product.objects.create(
            name          = data.get('name'),
            color         = data.get('color'),
            ram           = data.get('ram'),
            memory        = data.get('memory'),
            price         = data.get('price'),
            image         = data.get('image'),
            released_date = date(int(released_year), int(released_month), int(released_day)),
            company       = company
        )
        return JsonResponse({'added_product': data})
        # except:
        #     return JsonResponse({'status': 'bad'})