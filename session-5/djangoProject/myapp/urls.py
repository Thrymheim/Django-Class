# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.task_list, name='task_list'),
#     path('create/', views.task_create, name='task_create'),
#     path('update/<int:pk>/', views.task_update, name='task_update'),
#     path('delete/<int:pk>/', views.task_delete, name='task_delete'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
]
