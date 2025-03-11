from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_laptop, name='add_laptop'),
    path('edit/<int:pk>/', views.edit_laptop, name='edit_laptop'),
    path('delete/<int:pk>/', views.delete_laptop, name='delete_laptop'),
]
