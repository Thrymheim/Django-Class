from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_laptop, name='add_laptop'),
    path('laptop/<int:pk>/', views.laptop_detail, name='laptop_detail'),
    path('laptop/<int:pk>/feedback/', views.add_feedback, name='add_feedback'),
]
