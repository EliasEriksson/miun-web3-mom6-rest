from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import WebPage
from .serializers import WebPageSerializer


"""
A ViewSet class that controls whether a user is allowed to access the WebPage resource
how the WebPage recourse is serialized and how the WebPage data should be sorted
"""


class WebPageViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = WebPageSerializer
    queryset = WebPage.objects.all().order_by("order")
