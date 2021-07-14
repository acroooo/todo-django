from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('actualizar/<int:id>', views.actualizarTarea, name="actualizar")
]
