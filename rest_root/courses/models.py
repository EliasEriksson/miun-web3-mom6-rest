from django.db import models
from django.utils.html import strip_tags, conditional_escape


class Course(models.Model):
    university = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.FloatField()
    startDate = models.DateField()
    endDate = models.DateField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.university}: {self.name}"

    def save(self, *args, **kwargs):
        self.university = strip_tags(self.university)
        self.name = strip_tags(self.name)
        return super(Course, self).save(*args, **kwargs)
