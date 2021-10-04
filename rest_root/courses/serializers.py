from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"
        # exclude = ["user"]

    # @staticmethod
    # def get_user_id(course: Course) -> int:
    #     return course.user.user.id
