from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

# class CompanySerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Company
        # fields = ['id', 'company_name']


class UserSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'detail', 'completed', 'user', 'created_at', 'updated_at']
        # depth = 1



# todo.user
# todo.user.company