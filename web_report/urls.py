from django.urls import path
from web_report.views import report

urlpatterns = [
    path('', report, name='report'),

]
