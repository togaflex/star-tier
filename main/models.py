from django.db import models

# Create your models here.

class Company(models.Model):
    # The name of the company
    company_name = models.CharField(max_length=200)

    # The industrial nature of the company
    company_industry_choice = (
        ('SW', 'Software Driven'),
        ('HW', 'Hardware Driven'),
    )
    company_industry = models.CharField(
        max_length = 2,
        choices = company_industry_choice,
        default='SW',
    )

    def __str__(self):
        seq = (self.company_name, self.company_industry)
        return ' in '.join(seq)

class Job(models.Model):
    # Relationship with company
    job_company = models.ForeignKey(Company,
        on_delete=models.CASCADE)
    # Specific Role that this job offers
    job_role = models.CharField(max_length=200)
    # The location where this job is offered
    job_location = models.CharField(max_length=10)
    # The description of the job
    job_description = models.TextField()

    job_opened = models.DateTimeField("Date inserted to DB")

    def __str__(self):
        return self.job_role