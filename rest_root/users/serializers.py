from rest_framework import serializers
from .models import User


class UserProfileSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"
        # exclude = ["user"]

    # @staticmethod
    # def get_user_id(user: User) -> int:
    #     return user.user.id
