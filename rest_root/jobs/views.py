from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer


"""
A ViewSet class that controls whether a user is allowed to access the Job resource
how the Job recourse is serialized and how the Job data should be sorted
"""


class JobViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = JobSerializer
    queryset = Job.objects.all().order_by("order")
