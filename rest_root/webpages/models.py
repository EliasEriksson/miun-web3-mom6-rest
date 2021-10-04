from django.db import models
from users.models import User


class WebPage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    url = models.CharField(max_length=511)

    def __str__(self):
        return f"{self.title}"
