from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *


# Create your views here.
def index(request):
    tareas = Tarea.objects.all()
    
    form = TareaForm()
    
    # request
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    contexto = {
        'tareas': tareas, 
        'form': form
    }
    return render(request, 'tareas/lista.html', contexto)
