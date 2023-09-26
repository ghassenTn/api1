from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters , status
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer , UserSerializerAge
from django.http.response import JsonResponse
from . import serializers
def api(request):
    return HttpResponse('hello from api project')
# Create your views here.
def getapi(request):
    data = {
        'name':'ghassen',
        'age':22
    }
    return JsonResponse(data)
def getapifromdata(request):
    data = User.objects.all()
    response = {
        'users':list(data.values('name','email','age'))
    }
    return  JsonResponse(response)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class FBV_view(APIView):
    def get(self, request):
        # Handle GET request to retrieve all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class AddUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
class UpdateUserView(APIView):
    def put(self, request, name):
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class GetUserByName(APIView):
    def get(self,request,name):
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response({'Error': 'User not found '}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        name = request.data.get('name')
        age = request.data.get('age')

        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response({'Error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.check_age(int(age)) != False:
            user.setNbLoggedin()
            user.save()
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
