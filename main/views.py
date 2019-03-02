from django.shortcuts import render, get_object_or_404
from .models import Company, Job
from django.template import loader
from django.http import Http404

# Create your views here.
from django.http import HttpResponse

def home(request):
    company_list = Company.objects.order_by('-company_name')[:]
    context = {
        'company_name_list': company_list,
    }
    return render(request,'main/index.html', context)

# Return detail jobs of company
def detail(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    jobs = company.job_set.all()
    context = {'company':company, "jobs": jobs}
    return render(request, 'main/detail.html', context)

# def description(request, company_id):
#     response = "You're looking at description of company id %s."
#     return HttpResponse(response % company_id)

# Return industry specificiation of the company

def industry(request, company_id):
    company = Company.objects.get(id=company_id)
    response = "You're looking at industry of company which is %s."
    return HttpResponse(response % company.company_industry)