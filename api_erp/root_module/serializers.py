from root_module.models import Company, Users,Storage
from rest_framework import serializers




class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    storages = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_storages(self, obj):
        storages = Storage.objects.filter(company=obj)
        return StorageSerializer(storages, many=True).data
        
class UserDataSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    storage = StorageSerializer(read_only=True)
    class Meta:
        model = Users
        depth = 1
        exclude = ['password']


      


