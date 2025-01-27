from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    #When we make view dynamic we should dynamic URL as well!!!
    path('dynamicGreet/<str:name>/<str:lastname>/<str:age>/<str:city>/', views.dynamicGreet, name='dynamicGreet'),
    path('current-time/', views.current_time, name='current_time'),
    path('list-items/', views.list_items, name='list_items'),
]

