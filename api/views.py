from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets 
from .serializers import StudentSerializer 
from .models import Student 

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = Student.objects.all() 
      
    # specify serializer to be used 
    serializer_class = StudentSerializer 
