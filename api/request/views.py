from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from fuzzywuzzy import fuzz

import api.account.models as account_models
import api.camp.models as camp_models
from . import serializers
from . import models


class CreateRequestView(APIView):
    serializer_class = serializers.RequestSerializer

    def get(self, request: Request):
        child_id = request.query_params.get("child_id")
        camp_event_id = request.query_params.get("camp_event_id")
        
        if not child_id or not camp_event_id:
            return Response(
                {
                    "detail": "Некорректный запрос"
                },
                status.HTTP_400_BAD_REQUEST
            )
        
        child = get_object_or_404(
            account_models.ChildModel,
            pk=child_id
        )
        camp_event = get_object_or_404(
            camp_models.CampEventModel,
            pk=child_id
        )
        representative = get_object_or_404(
            account_models.RepresentativeModel,
            user=request.user
        )
        
        if not representative.check_child(child):
            return Response(
                {
                    "detail": "Некорректный запрос"
                },
                status.HTTP_400_BAD_REQUEST
            )
        
        request = models.RequestModel.objects.create(
            child=child,
            camp_event=camp_event,
            representative=representative
        )
        
        serializer = self.serializer_class(
            request
        )
        
        return Response(
            serializer.data,
            status.HTTP_200_OK
        )
