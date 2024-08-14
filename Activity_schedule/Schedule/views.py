from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Activity
from .forms import ActivityForm

# Create your views here.

def index(request):
    
    activitys = Activity.objects.all().order_by('id')
    
    return render(request, 'Schedule/Schedule.html', {'activitys': activitys})

def about(request):
    
    return render(request, 'About/About.html', {})

def create_activity(request):
    
    if request.method == 'POST':
        try:
            form = ActivityForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Atividade criada com sucesso!')
                return redirect('atividades')
        except Exception as err:
            messages.error(request, f"Não foi possivel criar a atividade, devido a {str({err})}")
            return redirect('atividades')
    else:
        form = ActivityForm()   
        
    return render(request, 'Activity/Activity_form.html', {'form': form})

def activity_details(request, pk):
    
    activity = get_object_or_404(Activity, pk=pk)
    
    return render(request, 'activity/Activity.html', {'activity': activity})

def edit_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    
    if request.method == 'POST':
        try:
            form = ActivityForm(request.POST, instance=activity)
            if form.is_valid():
                form.save()
                messages.success(request, f'Atividade {activity} editada com sucesso!')
                return redirect('atividades')
        except Exception as err:
            messages.error(request, f"Não foi possivel editar a atividade, devido a {str({err})}")
            return redirect('atividades')
    else: 
        form = ActivityForm(instance=activity)
    return render(request, 'activity/Activity_form.html', {'form': form, 'edit': True, 'activity': activity})

def delete_activity(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
   
    if request.method == 'POST':
        try:
           activity.delete()
           messages.success(request, 'Atividade deletada com sucesso!')
           return redirect('atividades')
        except Exception as err:
            messages.error(request, f"Não foi possivel deletar a atividade, devido a {str({err})}")
            return redirect('atividades')
    else:
        return render(request, 'Activity/Confirm_delete.html', {'activity': activity})