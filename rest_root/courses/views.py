from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .models import Course
from users.models import User
from .serializers import CourseSerializer


class CoursesView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request: Request, user_id: int) -> Response:
        courses = Course.objects.filter(user_id=user_id)
        return Response(CourseSerializer(courses, many=True).data)

    @staticmethod
    def post(request: Request, user_id: int) -> Response:
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(pk=user_id)
            course = Course(user=user, **serializer.validated_data)
            course.save()
            return Response(serializer.validated_data, status=201)

        return Response(status=400)


class CourseView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request, course_id: int) -> Response:
        try:
            course = Course.objects.get(pk=course_id)
            return Response(CourseSerializer(course).data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400)

    @staticmethod
    def put(request: Request, course_id: int) -> Response:
        serializer = CourseSerializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(status=400)
            course = Course(pk=course_id, **serializer.validated_data)
            course.save()
            return Response(CourseSerializer(course).data, status=200)

        except ObjectDoesNotExist:
            return Response(status=400)

    @staticmethod
    def delete(request: Request, course_id: int) -> Response:
        try:
            Course.objects.get(pk=course_id).delete()
            return Response(status=200)
        except ObjectDoesNotExist:
            return Response(status=400)
