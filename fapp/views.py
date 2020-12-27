from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .models import Fapp
from .serializer import FappSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404 
# Create your views here.
class Fapp_List(APIView):

    def get(self,request):
        data=Fapp.objects.all()
        serial=FappSerializer(data,many=True)
        return Response(serial.data)
    def post(self,request):
        serial=FappSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)

class Fapp_Particular(APIView):
    
    def get_object(self,name):
        try:
            return Fapp.objects.get(name=name)
        except Fapp.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,name):
        pract=self.get_object(name)
        serial=FappSerializer(pract)            
        print("pawan")
        return Response(serial.data)



    
# @csrf_exempt        
# def  PFapp(request,naam):
#     if request.method=='GET':
#         try:
#             Fappo=Fapp.object.get(naam=naam);
#         except  Fapp.DoesNotExist:
#             return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
#         serial=FappSerializer(Fapp)
#         return JsonResponse(serial.data);    




