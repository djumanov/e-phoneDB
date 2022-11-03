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
                ram           = data.get('ram'),
                memory        = data.get('memory'),
                price         = data.get('price'),
                image         = data.get('image'),
                released_date = datetime.strptime(data.get('released_date'), '%Y-%m-%d').date(),
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



class UpdateCompanyView(View):
    def post(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            company: Company = Company.objects.get(id=id)
            data: dict = request.POST
            if data.get('name'):
                company.name = data.get('name')
            if data.get('logo'):
                company.logo = data.get('logo')
            if data.get('description'):
                company.description = data.get('description')
            if data.get('website'):
                company.website = data.get('website')
            company.save()
            return JsonResponse({'updated_company': company_convert_to_dict(company)})

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})


class UpdateProductView(View):
    def post(self, request: HttpRequest, id: int) -> JsonResponse:
        try:
            product: Product = Product.objects.get(id=id)
            data: dict = request.POST
            if data.get('name'):
                product.name = data.get('name')
            if data.get('color'):
                product.color = data.get('color')
            if data.get('ram'):
                product.ram = data.get('ram')
            if data.get('memory'):
                product.memory = data.get('memory')
            if data.get('price'):
                product.price = data.get('price')
            if data.get('image'):
                product.image = data.get('image')
            if data.get('released_date'):
                product.released_date = datetime.strptime(data.get('released_date'), '%Y-%m-%d').date()
            product.save()
            return JsonResponse({'updated_product': product_convert_to_dict(product)})

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})
            

        
class GetCompanyByNameView(View):
    def get(self, request: HttpRequest, name: str) -> JsonResponse:
        try:
            company: Company = Company.objects.get(name=name)
            return JsonResponse({'company': company_convert_to_dict(company)})
        
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'bad'})



class GetProductByNameView(View):
    def get(self, request: HttpRequest, name: str) -> JsonResponse:
        products = Product.objects.filter(name=name).all()
        product_json = {'products': []}
        for product in products:
            product_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'product': product_json})


class GetProductByColorView(View):
    def get(self, request: HttpRequest, color: str) -> JsonResponse:
        products = Product.objects.filter(color=color).all()
        product_json = {'products': []}
        for product in products:
            product_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'product': product_json})


class GetProductByRamView(View):
    def get(self, request: HttpRequest, ram: int) -> JsonResponse:
        products = Product.objects.filter(ram=ram).all()
        product_json = {'products': []}
        for product in products:
            product_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'product': product_json})


class GetProductByMemoryView(View):
    def get(self, request: HttpRequest, memory: int) -> JsonResponse:
        products = Product.objects.filter(memory=memory).all()
        product_json = {'products': []}
        for product in products:
            product_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'product': product_json})


class GetProductByPriceView(View):
    def get(self, request: HttpRequest, price: str) -> JsonResponse:
        products = Product.objects.filter(price=price).all()
        product_json = {'products': []}
        for product in products:
            product_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'product': product_json})



class GetProductByCompanyView(View):
    def get(self, request: HttpRequest, company: str) -> JsonResponse:
        products: list[Product] = Product.objects.filter(company__name=company)
        products_json = {'products': []}
        for product in products:
            products_json['products'].append(product_convert_to_dict(product))

        return JsonResponse({'products': products_json})
        