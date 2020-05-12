from django.urls import path
from web_store.views import store

urlpatterns = [
    path('', store, name='store'),

]
