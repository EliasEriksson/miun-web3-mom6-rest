from django.db import models


class WebPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    url = models.CharField(max_length=511)

    def __str__(self):
        return f"{self.title}"
