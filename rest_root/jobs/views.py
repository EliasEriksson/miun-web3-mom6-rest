from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from .models import Job
from .serializers import JobSerializer


class JobsView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request: Request, user_id: int) -> Response:
        jobs = Job.objects.filter(user=user_id)
        return Response(JobSerializer(jobs, many=True).data)

    @staticmethod
    def post(request: Request, user_id: int) -> Response:
        serializer = JobSerializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(status=400)
            user = User.objects.get(pk=user_id)
            job = Job(user=user, **serializer.validated_data)
            job.save()
            return Response(JobSerializer(job).data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400)


class JobView(APIView):
    @staticmethod
    def get(request, job_id: int) -> Response:
        try:
            job = Job.objects.get(pk=job_id)
            return Response(JobSerializer(job).data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400)

    @staticmethod
    def put(request: Request, job_id: int) -> Response:
        serializer = JobSerializer(data=request.data)
        try:
            if not serializer.is_valid():
                return Response(status=400)
            job = Job(pk=job_id, **serializer.validated_data)
            job.save()
            return Response(JobSerializer(job).data, status=200)
        except ObjectDoesNotExist:
            return Response(status=400)

    @staticmethod
    def delete(request: Request, job_id: int) -> Response:
        try:
            Job.objects.get(pk=job_id).delete()
            return Response(status=200)
        except ObjectDoesNotExist:
            return Response(status=400)


