from datetime import datetime
from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Company, Product
from django.core.exceptions import ObjectDoesNotExist


def product_convert_to_dict(product: Product) -> dict:
    try:
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
    except ObjectDoesNotExist:
        return False


def company_convert_to_dict(company: Company) -> dict:
    company_dict = {
        'id': company.id,
        'logo': company.logo,
        'description': company.description,
        'website': company.website,
    }
    return company_dict




class CompaniesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        companies = Company.objects.all()
        companies_json = dict()
        for company in companies: 
            companies_json[company.name] = company_convert_to_dict(company)

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
            products_json['products'].append(product_convert_to_dict(product))

        return JsonResponse(data=products_json)


class CreateProductView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        data = request.POST
        company: Company = Company.objects.filter(name=data.get('company'))
        if company:
            product = Product.objects.create(
                name          = data.get('name'),
                color         = data.get('color'),
                ram           = int(data.get('ram')),
                memory        = int(data.get('memory')),
                price         = float(data.get('price')),
                image         = data.get('image'),
                released_date = datetime.strptime(str(data.get('released_date')), '%Y-%m-%d').date(),
                company       = company[0]
            )
            product.save()
            return JsonResponse({'added_product': data})

        return JsonResponse({'status': 'bad'})



class GetCompanyByIdView(View):
    def get(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            company: Company = Company.objects.get(id=id)
            return JsonResponse({'company': company_convert_to_dict(company)})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})



class GetProductByIdView(View):
    def get(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            product: Product = Product.objects.get(id=id)
            return JsonResponse({'product': product_convert_to_dict(product)})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})



class DeleteCompanyView(View):
    def post(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            company: Company = Company.objects.get(id=id)
            company_json = company_convert_to_dict(company)
            company.delete()
            return JsonResponse({'deleted_company': company_json})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})



class DeleteProductView(View):
    def post(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            product: Company = Product.objects.get(id=id)
            product_json = product_convert_to_dict(product)
            product.delete()
            return JsonResponse({'deleted_product': product_json})
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})