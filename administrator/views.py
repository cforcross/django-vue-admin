from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from common.serializers import UserSerializer
from core.models import User,Product,Link,OrderItem,Order
from common.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics,mixins
from .serializers import (ProductSerializer,LinkSerializer,OrderItemSerializer,OrderSerializer)

class AmbassadorAPiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors, many=True)
        return Response(serializer.data)


class ProductGenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()

    def get(self,request,pk=None, **kwargs):
        if pk:
            return self.retrieve(request,pk)
        return self.list(request)

    def post(self,request):
        return self.create(request)


    def put(self,request,pk=None, **kwargs):
        return self.partial_update(request,pk)

    def delete(self,request,pk=None):
        return self.destroy(request,pk)


class LinkAPiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request,pk=None):
        links = Link.objects.filter(user_id=pk)
        serializer = LinkSerializer(links, many=True)
        return Response(serializer.data)

class OrderAPIView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(complete=True)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)