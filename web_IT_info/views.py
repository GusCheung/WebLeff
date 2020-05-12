from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
import hashlib  # MD5解密

from django.views.decorators.csrf import csrf_exempt
import datetime
from django.contrib import messages


def IT_info(request):
    return HttpResponse("IT信息页")
