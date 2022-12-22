from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# Create your views here.


@api_view(['GET'])#READ
def home(request):
    Patient_obj=Patient.objects.all()
    serializer=Patientserializer(Patient_obj,many=True)
    return Response(serializer.data)

@api_view(['POST'])#CREATE
def create_home(request):
    serializer = Patientserializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)

@api_view(['POST'])#UPDATE
def update_home(request,id):
    Patient_obj = Patient.objects.get(id=id)
    serializer = Patientserializer(instance=Patient_obj,data=request.data)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])#DELETE
def delete_home(request,id):
    Patient_obj=Patient.objects.get(id=id)
    Patient_obj.delete()
    return Response('item deleted succesfully....!')

@api_view(['GET'])#View
def view_home(request,id):
    Patient_obj = Patient.objects.get(id=id)
    serializer = Patientserializer(Patient_obj)
    return Response(serializer.data)
