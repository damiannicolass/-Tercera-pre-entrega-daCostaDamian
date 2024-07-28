from django.urls import path
from appseguros.views import *

#path de models
urlpatterns = [
    path('', inicio, name="inicio"),
    path('empleados/', empleados, name="empleados"),
    path('asegurados/', asegurados, name="asegurados"),
    path('vehiculos/', vehiculos, name="vehiculos"),
    path('tareas/', tareas, name="tareas"),
    path('siniestros/', siniestros, name="siniestros"),
]

#paht de formularios
formularios  = [
    path('tareaFormulario/', tareaFormulario, name="tareaFormulario"),
    path('empleadoFormulario/', empleadoFormulario, name="empleadoFormulario" ),
    path('aseguradoFormulario/', aseguradoFormulario, name="aseguradoFormulario" ),
    path('vehiculoFormulario/', vehiculoFormulario, name="vehiculoFormulario" ),
    path('siniestroFormulario/', siniestroFormulario, name="siniestroFormulario" ),
]

urlpatterns += formularios

#path de busquedas
busquedas = [
    path("busquedaTarea/", busquedaTarea, name="busquedaTarea"),
    path("resultadoBusquedaTarea/", resultadoBusquedaTarea, name="resultadoBusquedaTarea"),
    path("busquedaEmpleado/", busquedaEmpleado, name="busquedaEmpleado"),
    path("resultadoBusquedaEmpleado/", resultadoBusquedaEmpleado, name="resultadoBusquedaEmpleado"),
    path("busquedaAsegurado/", busquedaAsegurado, name="busquedaAsegurado"),
    path("resultadoBusquedaAsegurado/", resultadoBusquedaAsegurado, name="resultadoBusquedaAsegurado"),
    path("busquedaVehiculo/", busquedaVehiculo, name="busquedaVehiculo"),
    path("resultadoBusquedaVehiculo/", resultadoBusquedaVehiculo, name="resultadoBusquedaVehiculo"),
    path("busquedaSiniestro/", busquedaSiniestro, name="busquedaSiniestro"),
    path("resultadoBusquedaSiniestro/", resultadoBusquedaSiniestro, name="resultadoBusquedaSiniestro"),
]

urlpatterns += busquedas