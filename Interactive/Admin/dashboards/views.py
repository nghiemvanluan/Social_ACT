import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from velzon.views import access_token


get_tags_url = 'http://45.119.82.5:8088/social/api/get_tags'


# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    pass


dashboard_view = DashboardView.as_view(template_name="dashboards/index.html")
dashboard_analytics_view = DashboardView.as_view(
    template_name="dashboards/dashboard-analytics.html")
dashboard_crm_view = DashboardView.as_view(
    template_name="dashboards/dashboard-crm.html")
dashboard_crypto_view = DashboardView.as_view(
    template_name="dashboards/dashboard-crypto.html")
dashboard_projects_view = DashboardView.as_view(
    template_name="dashboards/dashboard-projects.html")
# ---------------------------------------------


def dashboards(request):
    tag = requests.get(get_tags_url).json()
    print(1111111)
    print(tag)
    return render(request, 'dashboards/index.html', {'tag': tag})
