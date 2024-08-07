from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='atividades'),
   path('activity/new', views.create_activity, name='criar atividade'),
   path('activity/<int:id>', views.activity_details, name='detalhes de atividade'),
   
]