from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from root_module.permissions import HasModulePermission
from root_module.models import Module, RiskClass
from .serializers import StockSerializer, RiskClassSerializer, HistorySerializer
from .models import Stock
from rest_framework import status
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

 
class StockView(generics.ListAPIView):
    module_name = Module.STOCK_MANAGEMENT
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasModulePermission]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        class_data = RiskClass.objects.all()
        dts = Stock.objects.filter(company_id=request.user.company.id)
        data = StockSerializer(dts, many=True)
        risk = RiskClassSerializer(class_data, many=True)
        return Response({'data':data.data, 'classe_de_risco': risk.data})
    
    def post(self, request, *args, **kwargs):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    



class History(APIView):
    module_name = Module.STOCK_MANAGEMENT
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasModulePermission]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        stock_history = Stock.objects.filter(company_id=request.user.company.id)
        serializer = HistorySerializer(stock_history, many=True)
        serialized_data = serializer.data
        filtered_data = []
        for data in serialized_data:
            if data['history'] is not None and len(data['history']) > 0:
                filtered_data.append(data)
        return Response({"data": filtered_data})




class StockViewAnalitics(APIView):
    module_name = Module.STOCK_MANAGEMENT
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasModulePermission]
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer    
    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    


