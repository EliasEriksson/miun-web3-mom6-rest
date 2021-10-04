from django.db import models


class Course(models.Model):
    university = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.FloatField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return f"{self.university}: {self.name}"
