from django.db import models
from users.models import User


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    credit = models.FloatField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return f"{self.university}: {self.name}"
