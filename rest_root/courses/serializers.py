from rest_framework import serializers
from .models import Course

"""
Serializer class that helps converting JSON 
to a Course model and the other way around
"""


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "university", "name", "credit", "startDate", "endDate", "order"]
