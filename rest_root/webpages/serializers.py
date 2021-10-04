from rest_framework import serializers
from .models import WebPage


class WebPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WebPage
        fields = "__all__"
