from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    max_concurrent_users = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Module(models.Model):
    STOCK_MANAGEMENT = 'SM'
    PERSONNEL_DEPARTMENT_MANAGEMENT = 'PDM'
    HUMAN_RESOURCE_MANAGEMENT = 'HRM'
    PURCHASING_MANAGEMENT = 'PM'
    SALES_MANAGEMENT = 'SM'
    MODULE_CHOICES = [
        (STOCK_MANAGEMENT, 'Stock Management'),
        (PERSONNEL_DEPARTMENT_MANAGEMENT, 'Personnel Department Management'),
        (HUMAN_RESOURCE_MANAGEMENT, 'Human Resource Management'),
        (PURCHASING_MANAGEMENT, 'Purchasing Management'),
        (SALES_MANAGEMENT, 'Sales Management')
    ]

    name = models.CharField(max_length=3, choices=MODULE_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.company.name}'


class Users(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)
    modules = models.ManyToManyField(Module, blank=True)
   
    

class Storage(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False) 


class RiskClass(models.Model):
    consequencia = models.CharField(max_length=200)
    avali = models.CharField(max_length=200)
    risk = models.CharField(max_length=200)
