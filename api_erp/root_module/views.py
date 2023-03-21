from root_module.models import Users, Company, Storage
from rest_framework.decorators import api_view
from django.http import HttpResponse
from root_module.serializers import UserDataSerializer, CompanySerializer, StorageSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView



# TODO 
# CRIAR COMPANHIA

#DELETAR COPANHIA
        
