from django.db import models
from django.utils.html import strip_tags


class Job(models.Model):
    """
    model that represents the table in the database
    the model can be used to interact with CRUD operations
    on the Job table.
    """
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField(blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return f"{self.company}: {self.title}"

    def save(self, *args, **kwargs):
        self.company = strip_tags(self.company)
        self.title = strip_tags(self.title)
        return super(Job, self).save(*args, **kwargs)
