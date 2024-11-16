from django.urls import path
from . import views
 
urlpatterns =[
    path('', views.index, name ='index'), #if we call nothing in url, call index func
    path('home/', views.home, name='home'),
    #the path that is used to send data from front to backend
    path('getResponse', views.getResponse, name='getResponse')
]
