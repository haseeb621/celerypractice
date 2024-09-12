from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('Add',Add,name='Add'),
    path('about',Subtract,name='Subtract'),
    path('result/<str:task_id>',check_result,name='check_result'),
]
