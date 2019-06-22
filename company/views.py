from django.shortcuts import render
from .models import Stock
from .serializer import Stockserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class StockList(APIView):
    def get(self,request):
        stocks = Stock.objects.all()
        serializer = Stockserializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass