from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name

class Job(models.Model):
    job_role = models.CharField(max_length=200)
    job_location = models.CharField(max_length=10)
    job_description = models.TextField()
    job_opened = models.DateTimeField("date opened")

    def __str__(self):
        return self.job_role