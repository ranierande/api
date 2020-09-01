from django.urls import include, path 
from rest_framework import routers 
  
from .views import *
  
# define the router 
router = routers.DefaultRouter() 
  
# define the router path and viewset to be used 
router.register(r'student', StudentViewSet) 
  
# specify URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')) 
] 