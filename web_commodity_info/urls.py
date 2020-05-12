from django.urls import path
from web_commodity_info.views import commodity_info

urlpatterns = [
    path('', commodity_info, name='commodity_info'),

]
