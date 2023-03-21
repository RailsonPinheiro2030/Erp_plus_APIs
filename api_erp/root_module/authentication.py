from root_module.models import Users, Company, Storage
from django.http import HttpResponse
from root_module.serializers import UserDataSerializer, CompanySerializer, StorageSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView



class CustomAuth(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        values = Users.objects.filter(username=request.data['username'])
        data = UserDataSerializer(values, many=True)
        user_data = data.data[0]
        response.data['first_name'] = user_data['first_name']
        response.data['last_name'] = user_data['last_name']
        response.data['email'] = user_data['email']
        response.data['is_admin'] = user_data['is_admin']
        response.data['is_active'] = user_data['is_active']
        response.data['company'] = user_data['company']['name']
        response.data['company_id'] = user_data['company']['id']
        response.data['storages'] = user_data['company']['storages']
        return response