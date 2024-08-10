from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='atividades'),
   path('about/', views.about, name='about'),
   path('new/', views.create_activity, name='create'),
   path('<int:pk>/', views.activity_details, name='read'),
   path('<int:pk>/update/', views.edit_activity, name='update'),
   path('delete/<int:pk>', views.delete_activity, name='delete'),
   
]