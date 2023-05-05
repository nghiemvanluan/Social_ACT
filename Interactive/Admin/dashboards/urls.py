from django.urls import path
from .views import dashboards


urlpatterns = [
    path('', dashboards, name="dashboard"),
]
