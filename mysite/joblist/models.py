from django.db import models


class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=30)
    date = models.DateField(null=True)
