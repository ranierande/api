from rest_framework import serializers 
  
# import model from models.py 
from .models import Student
  
# Create a model serializer  
class StudentSerializer(serializers.HyperlinkedModelSerializer): 
    # specify model and fields 
    class Meta: 
        model = Student
        fields = ('title', 'description') 