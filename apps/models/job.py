from django.db import models
from .user import Employer


class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    salary = models.FloatField()

    def __str__(self):
        return self.title
