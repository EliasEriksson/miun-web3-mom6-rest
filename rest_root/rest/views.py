from typing import Type, Any
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer


class CRView(APIView):
    model: Type[Model]
    serializer: Type[ModelSerializer]

    @classmethod
    def get(cls, request: Request, **kwargs: {str: Any}) -> Response:
        try:
            objects = cls.model.objects.filter(**kwargs)
            return Response(cls.serializer(objects, many=True).data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400)

    @classmethod
    def post(cls, request: Request, **kwargs: {str: Any}) -> Response:
        serializer = cls.serializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(status=400)
            for key, value in kwargs.items():
                if key.endswith("_id"):
                    obj = cls.model(pk=value, **serializer.validated_data)
                    obj.save()
                    return Response(cls.serializer(obj).data, status=200)
            else:
                return Response(status=400)
        except ObjectDoesNotExist:
            return Response(status=400)
