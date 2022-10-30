from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Company, Product
import json


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
