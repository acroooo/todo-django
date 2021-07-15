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

# Eliminar tarea
def eliminarTarea(req, id):
    item = Tarea.objects.get(id=id)
    
    if req.method == 'POST':
        item.delete()
        return redirect('/')
    
    contexto = {
        'item': item,
    }
    
    return render(req, 'tareas/eliminar_tarea.html', contexto)

# Actualizar tarea
def actualizarTarea(req, id):
    tarea = Tarea.objects.get(id=id)
    
    form = TareaForm(instance=tarea)
    
    
    if req.method == 'POST':
        form = TareaForm(req.POST, instance=tarea)
        
        if form.is_valid():
            form.save()
            return redirect('/')
        
        
    contexto = {'form': form}
    return render(req, 'tareas/actualizar_tarea.html', contexto)
