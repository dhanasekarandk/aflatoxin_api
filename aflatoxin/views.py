from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.


class Testfunction(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,format=None):
        return Response({"data":[],"message":"Hai welcome to aflatoxin","status":True},status=status.HTTP_200_OK)

    def post(self,request,format=None):
        return Response({"data":[],"message":"Hai welcome to aflatoxin","status":True},status=status.HTTP_200_OK)

    def put(self,request,id,format=None):
        return Response({"data":id,"message":"Hai welcome to aflatoxin","status":True},status=status.HTTP_200_OK)

    def delete(self,request,id,format=None):
        return Response({"data":id,"message":"Hai welcome to aflatoxin","status":True},status=status.HTTP_200_OK)