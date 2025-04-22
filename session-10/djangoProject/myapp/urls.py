from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('csv/', views.produce_csv, name='produce_csv'),
    path('pdf/', views.generate_pdf, name='generate_pdf'),
]
