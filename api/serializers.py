from rest_framework import serializers
from .models import ModelOne


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelOne
        fields = ('__all__')
