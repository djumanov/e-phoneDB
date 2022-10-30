from django.contrib import admin
from .models import Company, Product


tables = [Company, Product]

admin.site.register(model_or_iterable=tables)
