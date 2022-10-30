from django.db import models


class Company(models.Model):
    name        = models.CharField(max_length=100)
    logo        = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    website     = models.CharField(max_length=100)


    def __repr__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ram = models.IntegerField()
    memory = models.IntegerField()
    price = models.FloatField()
    image = models.CharField(max_length=250)
    released_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)


    def __repr__(self) -> str:
        return self.name