from rest_framework import serializers
from .models import search 

class search_serializer(serializers.ModelSerializer):
    class Meta :
        model=search
        fields='__all__'