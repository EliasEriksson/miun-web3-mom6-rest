from rest_framework import serializers
from .models import WebPage


class WebPageSerializer(serializers.ModelSerializer):
    # user_id = serializers.SerializerMethodField()

    class Meta:
        model = WebPage
        fields = "__all__"
        # exclude = ["user"]

    # @staticmethod
    # def get_user_id(web_page: WebPage) -> int:
    #     return web_page.user.user.id
