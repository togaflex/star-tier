from django.db import models

# Create your models here.

class Company(models.Model):
    # The name of the company
    company_name = models.CharField(max_length=200)

    # The industrial nature of the company
    # company_industry_choice = (
    #     ('SW', 'Software Driven'),
    #     ('HW', 'Hardware Driven'),
    # )
    # company_industry = models.CharField(
    #     max_length = 2,
    #     choices = company_industry_choice,
    #     default='SW',
    # )

    def __str__(self):
        return self.company_name

class Job(models.Model):
    # Relationship with company
    job_company = models.ForeignKey(Company,
        on_delete=models.CASCADE)

    # Specific Role that this job offers
    job_role = models.CharField(max_length=200)

    # The location where this job is offered
    job_location = models.CharField(max_length=10)

    # Minimum Qualification
    job_minimum_qual = models.TextField()

    # Prefered Qualification
    job_prefered_qual = models.TextField()

    # The description of the job
    job_description = models.TextField()

    # Time
    job_closed = models.DateTimeField("Date job will be closed")

    # Status
    job_status = models.BooleanField()

    # Link to page
    job_link = models.URLField(max_length=128)

    # Year eligible
    job_year = models.TextField()
    
    #Full time or not
    job_type_choice = (
         ('PT', 'Part-Time'),
         ('FT', 'Full-Time'),
    )
    job_type = models.CharField(
         max_length = 2,
         choices = job_type_choice,
         default='FT',
    )

    def min_qual_as_list(self):
        return self.job_minimum_qual.split('\n')

    def pre_qual_as_list(self):
        return self.job_prefered_qual.split('\n')
    
    def year_as_list(self):
        return self.job_year.split(',')

    def __str__(self):
        return self.job_role