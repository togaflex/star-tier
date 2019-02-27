from django.shortcuts import render

from .models import Company, Job
from django.template import loader
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

def home(request):
    company_list = Company.objects.order_by('-company_name')[:]
    template = loader.get_template('main/index.html')
    context = {
        'company_name_list': company_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        jobs = company.job_set.all()
    except Company.DoesNotExist:
        raise Http404("I made it: Company does not exist")
    template = loader.get_template('main/detail.html')
    context = {'company':company, "jobs": jobs}

    return HttpResponse(template.render(context, request))

def description(request, company_id):
    response = "You're looking at description of company id %s."
    return HttpResponse(response % company_id)

def industry(request, company_id):
    response = "You're looking at industry of company id %s."
    return HttpResponse(response % company_id)