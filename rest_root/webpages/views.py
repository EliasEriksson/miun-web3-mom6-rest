from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WebPage
from .serializers import WebPageSerializer


class WebPagesView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request: Request, user_id: int) -> Response:
        web_pages = WebPage.objects.filter(user=user)
        return Response(WebPageSerializer(web_pages, many=True).data)


class WebPageView(APIView):
    @staticmethod
    def get(request, job_id: int) -> Response:
        pass

    @staticmethod
    def put(request: Request, job_id: int) -> Response:
        pass

    @staticmethod
    def delete(request: Request, job_id: int) -> Response:
        pass
