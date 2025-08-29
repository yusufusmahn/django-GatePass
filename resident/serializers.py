from rest_framework import serializers

from resident.models import House, Invite

from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['house_number', 'address']



class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'phone']



class CreateInviteSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255, allow_blank=False)
    last_name = serializers.CharField(max_length=255, allow_blank=False)
    phone = serializers.CharField(max_length=11, min_length=11, allow_blank=False)
    expires_at = serializers.DateTimeField()



class VerifyInviteSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, min_length=6)


class InviteSerializer(serializers.ModelSerializer):
    house = HouseSerializer()

    class Meta:
        model = Invite
        fields = ['code', 'expires_at', 'created_at', 'status', 'house']

