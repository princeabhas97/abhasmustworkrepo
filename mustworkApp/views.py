from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import test2

@api_view(['POST'])
def my_views2(request):
    print('this is a request',request.data)
    firstname=request.data['firstname']
    lastname = request.data['lastname']
    email = request.data['email']
    standard=request.data['standard']
    emp=test2.objects.create(
        firstname=firstname,
        lastname=lastname,
        email=email,
        standard=standard,
    )
    return Response({"message": "this is test response of abhas project"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_views2(request, standard=None):
   # print('this is a request',request.data)
    firstname=request.GET.get('firstname')
    lastname = request.GET.get('lastname')
    email = request.data['email']
    standard = request.data['standard']
    emp=test2.objects.create(
        firstname=firstname,
        lastname=lastname,
        email=email,
   standard = standard,
    )
    return Response({"message": "this is test response of abhas project"}, status=status.HTTP_200_OK)