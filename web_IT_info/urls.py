from django.urls import path
from web_IT_info.views import IT_info

urlpatterns = [
    path('', IT_info, name='IT_info'),

]
