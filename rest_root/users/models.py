from django.db import models
from django.contrib.auth.models import User as InternalUser


class User(models.Model):
    user = models.OneToOneField(
        InternalUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
