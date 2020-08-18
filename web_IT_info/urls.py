from django.urls import path
from web_IT_info.views import IT_info, IT_info_lctzbm
urlpatterns = [
    path('', IT_info, name='IT_info'),
    path('<lctzbm>/', IT_info_lctzbm, name='IT_info_lctzbm'),

]
