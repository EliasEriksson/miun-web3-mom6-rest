from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.request import Request
from .models import User
from .serializers import UserProfileSerializer


class UserView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @staticmethod
    def get(request: Request) -> Response:
        users = User.objects.all()
        return Response(UserProfileSerializer(users, many=True).data)
