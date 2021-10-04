from django.db import models


class Job(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def __str__(self):
        return f"{self.company}: {self.title}"
