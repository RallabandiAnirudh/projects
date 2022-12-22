from django.contrib import admin
from django.urls import path
from .views import home,create_home,update_home,delete_home,view_home

urlpatterns = [
    path('',home,name='home'),
    path('create-home/',create_home,name='create'),
    path('update-home/<int:id>/',update_home,name='update'),
    path('delete-home/<int:id>/', delete_home, name='delete'),
    path('view-home/<int:id>/', view_home, name='view'),
]
