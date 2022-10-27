from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    permissions = serializers.CharField()
    is_active = serializers.BooleanField()
    
    class Meta:
        model = User
        fields = ['username', 'permissions']
