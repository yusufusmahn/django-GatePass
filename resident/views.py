from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, House, Invite, Visitor
from rest_framework.permissions import IsAuthenticated
from .models import House
from .serializers import HouseSerializer, CreateInviteSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_house(request):
    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = request.user
    user = get_object_or_404(User, pk=user.pk)
    if user.is_resident:
        House.objects.create(
            house_number=serializer.validated_data['house_number'],
            address=serializer.validated_data['address'],
            user=user
        )

        return Response(data={"message": "house added successfully"}, status=status.HTTP_201_CREATED)

    return Response(data={"message": "Not allowed"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_invite(request):
    user = request.user
    if user.is_resident:
        serializer = CreateInviteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        house = get_object_or_404(House, user_id=user.pk)
        invite = Invite()
        invite.house = house
        invite.expires_at=serializer.validated_data['expires_at'],

        Visitor.objects.create(
            first_name=serializer.validated_data['first_name'],
            last_name=serializer.validated_data['last_name'],
            phone_number=serializer.validated_data['phone_number'],
            invite=invite,
        )

        code = invite.code
        return Response(data={"code": code}, status=status.HTTP_201_CREATED)
    return Response(data={"message": "Not Authorized"}, status=status.HTTP_403_FORBIDDEN)