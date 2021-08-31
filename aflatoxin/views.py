from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework import status
from django.db import connection

# Create your views here.

#################
#COMMON METHODS#
# cursor to dictionary
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return rows

#################

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


class AflatoxinCropList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,format=None):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT 
            * from toxin_warehouse.CROP_LIST""")
            crop_list=dictfetchall(cursor)
        return Response({
                'code':200,
                'status':True,
                'data':crop_list,
                'message':"Crop List Fetched Successfully."
        },status=status.HTTP_200_OK)

class ToxinList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request,format=None):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT 
            * from toxin_warehouse.TOXIN_LIST""")
            toxin_list=dictfetchall(cursor)
        return Response({
                'code':200,
                'status':True,
                'data':toxin_list,
                'message':"Crop List Fetched Successfully."
        },status=status.HTTP_200_OK)