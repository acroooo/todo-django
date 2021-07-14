from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.

# Vista de tareas (lista) y creacion de tarea.
def index(req):
    tareas = Tarea.objects.all()
    
    form = TareaForm()
    
    # request
    if req.method == 'POST':
        form = TareaForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    # contexto
    contexto = {
        'tareas': tareas, 
        'form': form
    }
    
    # render
    return render(req, 'tareas/lista.html', contexto)


# Actualizar tarea
def ActualizarTarea(req, id):
    tarea = Tarea.objects.get(id=id)
    return render(req, 'tareas/actualizar_tarea.html')