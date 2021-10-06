from django.db import models
from django.utils.html import strip_tags, conditional_escape


class WebPage(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    url = models.CharField(max_length=511)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.title = strip_tags(self.title)
        self.description = strip_tags(self.description)
        return super(WebPage, self).save(*args, **kwargs)
