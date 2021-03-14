from django.shortcuts import render,redirect
from .models import activity
from .forms import ActivityForm
# Create your views here.
def home(request):
    context={
        'activities':activity.objects.all()
    }
    return render(request,'Todo_List/home.html',context)

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Todo-home')
    else:
        form = ActivityForm()

    return render(request, 'Todo_List/add_activity.html', {'form': form})

def search_activity(request):
    if request.method == 'GET':
        act_name=request.GET['keyword']
        if act_name:
            context={
        'activities':activity.objects.filter(title=act_name)
    }
        else:
            context={
            'activities':activity.objects.all()
        }   
    return render(request,'Todo_List/home.html',context)



def delete_activity(request,pk):
    act = activity.objects.get(id=pk)
    act.delete()
    return redirect('Todo-home')
