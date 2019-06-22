from rest_framework import serializers
from .models import Stock

class Stockserializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'