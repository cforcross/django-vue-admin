from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from common.serializers import UserSerializer
from core.models import User,Product,Link,OrderItem,Order
from common.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductSerializer
from django.core.cache import cache
import time
# Create your views here.

class ProductFrontendAPIView(APIView):
    # authentication_classes =[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductBackendAPIView(APIView):
    def get(self, request):
        products = cache.get('products_backend')
        if not products:
            time.sleep(2)
            products = list(Product.objects.all())
            cache.set(products, 'products_backend',timeout=60*30)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)