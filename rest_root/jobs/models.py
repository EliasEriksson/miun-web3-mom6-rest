from django.db import models
from django.utils.html import strip_tags, conditional_escape


class Job(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.company}: {self.title}"

    def save(self, *args, **kwargs):
        self.company = strip_tags(self.company)
        self.title = strip_tags(self.title)
        return super(Job, self).save(*args, **kwargs)
