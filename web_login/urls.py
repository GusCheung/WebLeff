from django.urls import path
from web_login.views import login,index,user_logout,ding_login

urlpatterns = [
    path('', login, name='login'),
    path('index', index, name='index'),
    path('user_logout', user_logout, name='user_logout'),
    path('ding_login', ding_login, name='ding_login')
]
