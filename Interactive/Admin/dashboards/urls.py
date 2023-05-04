from django.urls import path
from dashboards.views import (
    dashboard_view,
    dashboard_analytics_view,
    dashboard_crm_view,
    dashboard_crypto_view,
    dashboard_projects_view
)

app_name = 'dashboards'

urlpatterns = [
    path('', view=dashboard_view, name="dashboard"),
    path('dashboard-analytics', view=dashboard_analytics_view,
         name="dashboard_analytics"),
    path('dashboard-crm', view=dashboard_crm_view, name="dashboard_crm"),
    path('dashboard-crypto', view=dashboard_crypto_view, name="dashboard_crypto"),
    path('dashboard-projects', view=dashboard_projects_view,
         name="dashboard_projects"),

]
