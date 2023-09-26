from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializerAge(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['age']
class UserSerializernbLoggedIn(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nbloggedin']