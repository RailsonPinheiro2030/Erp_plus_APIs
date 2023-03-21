from djongo import models
from datetime import datetime
from django.db.models.signals import pre_delete
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.dispatch import receiver


class Stock(models.Model):
    codigo = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    company_id = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    group_type = models.CharField(max_length=100)
    exit_price = models.FloatField()
    cost_price = models.FloatField()
    quantity_stock = models.IntegerField()
    storage = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    quantity_use = models.IntegerField()
    minimum_quantity_stock = models.IntegerField()
    Effect_Consequence_of_failure = models.IntegerField(default=0)
    potential_existing_risk = models.CharField(max_length=100, default='UNDEFINED')
    repairable = models.BooleanField(default=False)
    strategy_when_fails = models.CharField(max_length=100, default='UNDEFINED')
    Highest_criticality_of_assets = models.IntegerField(default=0)
    failure_frequency = models.CharField(max_length=100, default='UNDEFINED')
    cost_operation = models.FloatField(default=0)
    volume_production = models.FloatField(default=0)
    health_security = models.IntegerField(default=0)
    environment = models.IntegerField(default=0)
    lead_time_new = models.IntegerField(default=0)
    datatime = models.DateTimeField(auto_now_add=True)
    analysis_date = models.DateTimeField(null=True, blank=True)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if Stock.objects.filter(codigo=self.codigo, company_id=self.company_id).exclude(id=self.id).exists():
            raise ValidationError({'codigo': ['Este codigo já existe para esta empresa']})
        super().save(*args, **kwargs)
            