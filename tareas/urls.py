from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('actualizar/<str:id>', views.actualizarTarea, name="actualizar"),
    path('eliminar/<str:id>', views.eliminarTarea, name="eliminar")
]
