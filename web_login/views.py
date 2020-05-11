from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse

# Create your views here.


def login(request):
    return render(request, 'login.html')