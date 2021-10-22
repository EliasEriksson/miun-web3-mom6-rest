from rest_framework import serializers
from .models import WebPage


"""
Serializer class that helps converting JSON 
to a WebPage model and the other way around
"""


class WebPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebPage
        fields = ["id", "title", "description", "url", "order"]
