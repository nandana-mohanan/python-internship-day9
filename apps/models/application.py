from django.db import models
from .job import Job
from .user import Candidate


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')
