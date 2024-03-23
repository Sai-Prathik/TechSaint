from django.shortcuts import render
from django.http import request,JsonResponse
from rest_framework import status
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
import re

phone = re.compile( r'(\+\d{1,2}\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}')
email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
# token = Token.objects.create(user=...)
# print(token.key)

# Create your views here.

# def register(request):
#     return JsonResponse([{"res":'test'}],safe=False)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    # print(serializer.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token":token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def userDetailsExists(request): 
    match_key = request.query_params.get('match_key')
    user= User.objects.filter(email=match_key)
    if user:
        return Response({"status":0})
        
    return Response({"status":1})


@api_view(['POST'])
def login(request):  
    user=''
    user_id=request.data['user_id']
    if email.match(user_id):
        user = User.objects.get(email=user_id)
    else:
        user = User.objects.get(username=user_id) 
    if user:
        if user.password != request.data['password']:
            return Response({"message":"Incorrect credentials"},status=status.HTTP_200_OK)
        else:
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(instance=user)
            return Response({"message":"success", "token":token.key,"user":serializer.data},status=status.HTTP_200_OK)


    return Response({"message":"User not found"},status=status.HTTP_404_NOT_FOUND)
     
    

