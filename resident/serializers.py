from rest_framework import serializers



class HouseSerializer(serializers.Serializer):
    house_number = serializers.IntegerField()
    address = serializers.CharField(max_length=255)
    user = serializers.IntegerField()