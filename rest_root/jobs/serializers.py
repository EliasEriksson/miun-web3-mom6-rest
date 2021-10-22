from rest_framework import serializers
from .models import Job


"""
Serializer class that helps converting JSON 
to a Job model and the other way around
"""


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ["id", "company", "title", "startDate", "endDate", "order"]
