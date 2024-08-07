from django.shortcuts import render
from .models import Activity

# Create your views here.

def index(request):
    
    activity = Activity.objects.all().order_by('id')
    
    return render(request, 'Schedule/Schedule.html', {'activity': activity})

def create_activity(request):
    pass

def activity_details(request):
    pass