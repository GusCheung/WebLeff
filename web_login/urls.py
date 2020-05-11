from django.urls import path
from web_login.views import login

urlpatterns = [
    path('login', login, name='login')

]
