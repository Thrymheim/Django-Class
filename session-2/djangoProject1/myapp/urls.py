from django.urls import path
#This means we wanna use the views of this dierctory and give them addresses
from . import views

urlpatterns = [
 #we we put '' empty it means its our main page
 path('', views.interoduce, name='name'),
 path('about/', views.about, name='about'),
]
