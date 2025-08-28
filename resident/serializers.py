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



class CreateInviteSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, blank=False, null=False)
    last_name = serializers.CharField(max_length=255, blank=False, null=False)
    phone = serializers.CharField(max_length=11, min_length=11, blank=False, null=False)
    expires_at = serializers.DateTimeField(null=False, blank=False)