from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from fuzzywuzzy import fuzz

from api.requests import DadataAddressSearch
from api.account.countries import COUNTRIES
from . import serializers
from . import models


class AddressSearchView(APIView):
    def get(self, request: Request):
        search = request.query_params.get("search", "")
        limit = int(request.query_params.get("limit", 5))
        
        result = DadataAddressSearch.search(search=search, limit=limit)
        
        return Response(
            result,
            status.HTTP_200_OK
        )


class AddressGetView(APIView):
    def post(self, request: Request):
        result = DadataAddressSearch.get(request.data.get("address"))
        return Response(
            result,
            status.HTTP_200_OK
        )


class AddressView(APIView):
    serializer_class = serializers.AddressSerializer
    
    def post(self, request: Request):
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            serializer.data,
            status.HTTP_201_CREATED
        )



class CountryAutoCompleteView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request: Request):
        search = request.query_params.get("search", "")
        
        response = []
        
        if not search:
            return Response(
                response,
                status.HTTP_200_OK
            )
            
        for country in COUNTRIES:
            coincidence = fuzz.ratio(search.lower(), country[0].lower())
            response.append((country, coincidence))

            if coincidence == 100:
                return Response(
                    [country],
                    status.HTTP_200_OK
                )

        response = sorted(response, key=lambda value: value[1], reverse=True)[:5]

        return Response(
            list(map(
                lambda value: value[0][1],
                response
            )),
            status.HTTP_200_OK
        )
