from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings

from api.address.models import AddressModel
from . import serializers
from . import models


class GetRepresentativeView(APIView):
    serializer_class = serializers.RepresentativeSerializer

    def get(self, request: Request):
        serializer = self.serializer_class(
            self.get_representative(request.user)
        )
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )

    @staticmethod
    def get_representative(user):
        return get_object_or_404(
            models.RepresentativeModel,
            user=user
        )


class PassportView(APIView):
    serializer_class = serializers.RepresentativeSerializer

    def put(self, request: Request) -> Response:
        representative = GetRepresentativeView.get_representative(
            user=request.user
        )
        serializer = self.serializer_class(
            representative,
            request.data,
            partial=True
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
        

class ChildView(APIView):
    serializer_class = serializers.ChildSerializer
    
    def post(self, request: Request):
        representative = GetRepresentativeView.get_representative(
            user=request.user
        )
        
        address = get_object_or_404(
            AddressModel,
            pk=request.data.get("address_id")
        )
    
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid()
        child = serializer.save(address=address)

        representative.children.add(child)
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
    
    def get(self, request: Request):
        representative = GetRepresentativeView.get_representative(
            user=request.user
        )
        
        serializer = self.serializer_class(
            representative.children.all(),
            many=True
        )
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
        

class DetailChildView(APIView):
    serializer_class = serializers.ChildSerializer
    
    def delete(self, request: Request, pk: int):
        child: models.ChildModel = get_object_or_404(
            models.ChildModel,
            pk=pk
        )
        
        child.delete()
        
        return Response(
            {
                "detail": "Deleted"
            },
            status.HTTP_200_OK
        )
    
    def get(self, request: Request, pk: int):
        child = get_object_or_404(
            models.ChildModel,
            pk=pk
        )
        
        serializer = self.serializer_class(
            child
        )
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )


class AddressView(APIView):
    serializer_class = serializers.RepresentativeSerializer
    
    def put(self, request: Request):
        representative = GetRepresentativeView.get_representative(
            user=request.user
        )
        
        address = get_object_or_404(
            AddressModel,
            pk=request.data.get("address_id")
        )
        serializer = self.serializer_class(
            representative,
            request.data,
            partial=True
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save(address=address)
        
        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )
