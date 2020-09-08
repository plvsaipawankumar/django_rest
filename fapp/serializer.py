from rest_framework import serializers
from .models import Fapp

class FappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fapp
        fields='__all__';