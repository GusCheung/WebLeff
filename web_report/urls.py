from django.urls import path
from web_report.views import xxsj_report, export, push_run, push_commodity, push_production

urlpatterns = [
    path('xxsj_report', xxsj_report, name='xxsj_report'),
    path('push_run', push_run, name='push_run'),
    path('push_commodity', push_commodity, name='push_commodity'),
    path('push_production', push_production, name='push_production'),
    path('export', export, name='export ')

]
