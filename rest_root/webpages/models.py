from django.db import models
from django.utils.html import strip_tags


class WebPage(models.Model):
    """
    model that represents the table in the database
    the model can be used to interact with CRUD operations
    on the WebPage table.
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=511)
    url = models.CharField(max_length=511)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.title = strip_tags(self.title)
        self.description = strip_tags(self.description)
        return super(WebPage, self).save(*args, **kwargs)
