from django.db import models
from django.utils.html import strip_tags, conditional_escape


class Job(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return f"{self.company}: {self.title}"

    def save(self, *args, **kwargs):
        self.company = conditional_escape(strip_tags(self.company))
        self.title = conditional_escape(strip_tags(self.title))
        return super(Job, self).save(*args, **kwargs)
