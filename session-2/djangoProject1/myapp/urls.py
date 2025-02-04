from django.urls import path
from . import views

urlpatterns = [
 path('', views.interoduce, name='name'),
 path('about/', views.about, name='about'),
]
