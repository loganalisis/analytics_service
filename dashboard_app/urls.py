from django.urls import path
from .views import get_dashboard

urlpatterns = [
    path("dashboard/", get_dashboard),
]
