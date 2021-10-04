from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"
        # exclude = ["user"]

    # @staticmethod
    # def get_user_id(job: Job) -> int:
    #     return job.user.user.id
