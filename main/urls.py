from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    # ex: /main/
    path("", views.home, name='home'),
    # ex: /main/5/
    path('<int:company_id>/', views.detail, name = 'detail'),
    # ex: /main/5/des
    path('<int:company_id>/des/', views.description, name = "description"),
    # ex: /main/5/industry
    path('<int:company_id>/industry/', views.industry, name = "industry"),
]