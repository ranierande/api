from django.contrib import admin  
from django.urls import path, include 
  
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    # add apis urls 
    path('', include("api.urls")) 
] 