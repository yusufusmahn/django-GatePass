from rest_framework import serializers

from resident.models import House

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['house_number', 'address']



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']

