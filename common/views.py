from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from .serializers import UserSerializer
from core.models import User
from common.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        print('data above')

        if data['password'] != data["password_confirm"]:
            raise exceptions.APIException("passwords don't match!")

        data['is_ambassador']='api/ambassador' in request.path

        serializer = UserSerializer(data=data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPI(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed("user not found")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Incorect password")

        scope = 'ambassador' if 'api/ambassador' in request.path else 'admin'

        if user.is_ambassador and scope =='admin':
            raise exceptions.AuthenticationFailed("Unauthorized")

        token = JWTAuthentication.generate_jwt(user.id,scope)

        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data ={
            'message':"success"
        }
        return response

class UserApiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    
    def get(self, request):
        user = request.user
        data = UserSerializer(request.data).data
        if 'api/ambassador' in request.path:
            data['revenue']= user.revenue
        return Response(data)


class LogoutApiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def post(self, request):
        response = Response.delete_cookie(key='jwt')
        response.data ={
            "message":"success"
        }
        return response


class ProfileInfoApiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def put(self, request,pk=None):
        user = request.user
        serializer = UserSerializer(user,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PasswordApiView(APIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def put(self, request,pk=None):
        user = request.user
        data = request.data

        if data['password'] != data["password_confirm"]:
            raise exceptions.APIException("passwords don't match!")
        user.set_password(data["password"])
        user.save()
        return Response(UserSerializer(user).data)