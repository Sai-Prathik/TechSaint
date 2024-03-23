from django.shortcuts import render
from django.http import request,JsonResponse
# Create your views here.

def post_content(request):
    return JsonResponse([{'res':'test'}],safe=False)