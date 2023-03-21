# from root_module.models import Company, Users,Storage
from rest_framework import serializers
from .models import Stock
from root_module.models import RiskClass

class RiskClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskClass
        fields = '__all__'

class HistoricalStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock.history.model
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    history = HistoricalStockSerializer(many=True, read_only=True)
    class Meta:
        model = Stock
        fields = ['history']




