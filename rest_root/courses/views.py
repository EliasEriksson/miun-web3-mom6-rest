from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Course
from .serializers import CourseSerializer


"""
A ViewSet class that controls whether a user is allowed to access the Course resource
how the Course recourse is serialized and how the Course data should be sorted
"""


class CourseViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by("order")
