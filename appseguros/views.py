from django.shortcuts import render, redirect
from django.http import HttpResponse
from appseguros.forms import *

from .models import *

# Create your views here.
def inicio(request):
    return render(request, "appseguros/inicio.html")

def empleados(request):
    return render(request, "appseguros/empleados.html")

def asegurados(request):
    return render(request, "appseguros/asegurados.html")

def vehiculos(request):
    return render(request, "appseguros/vehiculos.html")

def tareas(request):
    return render(request, 'appseguros/tareas.html')

def siniestros(request):
    return render(request, 'appseguros/siniestros.html')

#Empleados
def busquedaEmpleado(request):
    return render (request, "appseguros/busquedaEmpleado.html")

def resultadoBusquedaEmpleado(request):
    return render (request, "appseguros/resultadoBusquedaEmpleado.html")

#Asegurados
def busquedaAsegurado(request):
    return render (request, "appseguros/busquedaAsegurado.html")

def resultadoBusquedaAsegurado(request):
    return render (request, "appseguros/resultadoBusquedaAsegurado.html")

#Vehiculo
def busquedaVehiculo(request):
    return render (request, "appseguros/busquedaVehiculo.html")

def resultadoBusquedaVehiculo(request):
    return render (request, "appseguros/resultadoBusquedaVehiculo.html")

#Tareas
def busquedaTarea(request):
    return render (request, "appseguros/busquedaTarea.html")

def resultadoBusquedaTarea(request):
    return render (request, "appseguros/resultadoBusquedaTarea.html")

#Siniestros
def busquedaSiniestro(request):
    return render (request, "appseguros/busquedaSiniestro.html")

def resultadoBusquedaSiniestro(request):
    return render (request, "appseguros/resultadoBusquedaSiniestro.html") 




#EMPLEADOS
#mostramos todos los empleados
def empleados(request):
    empleados = Empleado.objects.all()  # Obtiene todos los empleados
    return render(request, 'appseguros/empleados.html', {'empleados': empleados})


#Formulario de empleados pendientes para agregar a la base de datos
def empleadoFormulario (request):
    if request.method == "POST":
        mi_formulario = EmpleadoFormulario(request.POST) #Aca llega la info del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            empleado = Empleado(nombre=informacion["nombre"], apellido=informacion["apellido"])
            empleado.save()
            
            return redirect('empleados') 
    else:
        mi_formulario = EmpleadoFormulario()
    
    return render(request, "appseguros/empleadoFormulario.html", {"mi_formulario": mi_formulario})


#muestra resultado de la busqueda de empleados
def resultadoBusquedaEmpleado(request):
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        empleados = Empleado.objects.filter(nombre__icontains=nombre)  
        
        return render(request, "appseguros/resultadoBusquedaEmpleado.html", {"nombre": nombre, "empleados": empleados})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



#ASEGURADOS
#mostramos todos los asegurados
def asegurados(request):
    asegurados = Asegurado.objects.all()  # Obtiene todos los asegurados
    return render(request, 'appseguros/asegurados.html', {'asegurados': asegurados})


#Formulario de asegurados pendientes para agregar a la base de datos
def aseguradoFormulario (request):
    if request.method == "POST":
        mi_formulario = AseguradoFormulario(request.POST) #Aca llega la info del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            asegurado = Asegurado(nombre=informacion["nombre"], apellido=informacion["apellido"],dni=informacion["dni"])
            asegurado.save()
            
            return redirect('asegurados') 
    else:
        mi_formulario = AseguradoFormulario()
    
    return render(request, "appseguros/aseguradoFormulario.html", {"mi_formulario": mi_formulario})


#muestra resultado de la busqueda de asegurados
def resultadoBusquedaAsegurado(request):
    if "nombre" in request.GET:
        nombre = request.GET["nombre"]
        asegurados = Asegurado.objects.filter(nombre__icontains=nombre)  
        
        return render(request, "appseguros/resultadoBusquedaAsegurado.html", {"nombre": nombre, "asegurados": asegurados})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



#VEHICULOS
#mostramos todos los vehiculos
def vehiculos(request):
    vehiculos = Vehiculo.objects.all()  # Obtiene todos los vehiculos
    return render(request, 'appseguros/vehiculos.html', {'vehiculos': vehiculos})


#Formulario de vehiculos para agregar a la base de datos
def vehiculoFormulario (request):
    if request.method == "POST":
        mi_formulario = VehiculoFormulario(request.POST) #Aca llega la info del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            vehiculo = Vehiculo(dominio=informacion["dominio"], año=informacion["año"], numero_motor=informacion["numero_motor"])
            vehiculo.save()
            
            return redirect('vehiculos') 
    else:
        mi_formulario = VehiculoFormulario()
    
    return render(request, "appseguros/vehiculoFormulario.html", {"mi_formulario": mi_formulario})


#muestra resultado de la busqueda de vehiculos
def resultadoBusquedaVehiculo(request):
    if "dominio" in request.GET:
        dominio = request.GET["dominio"]
        vehiculos = Vehiculo.objects.filter(dominio__icontains=dominio)  
        
        return render(request, "appseguros/resultadoBusquedaVehiculo.html", {"dominio": dominio, "vehiculos": vehiculos})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)



#TAREAS
#mostrar tareas pendientes
def tareas(request):
    tareas = Tarea.objects.all()  # Obtiene todas las tareas
    return render(request, 'appseguros/tareas.html', {'tareas': tareas})


#Formulario de tareas pendientes para agregar a la base de datos
def tareaFormulario (request):
    if request.method == "POST":
        mi_formulario = TareaFormulario(request.POST) #Aca llega la info del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            tarea = Tarea(titulo=informacion["titulo"], subtitulo=informacion["subtitulo"])
            tarea.save()
            
            return redirect('tareas') 
    else:
        mi_formulario = TareaFormulario()
    
    return render(request, "appseguros/tareaFormulario.html", {"mi_formulario": mi_formulario})


#muestra resultado de la busqueda de tareas
def resultadoBusquedaTarea(request):
    if "titulo" in request.GET:
        titulo = request.GET["titulo"]
        tareas = Tarea.objects.filter(titulo__icontains=titulo)  
        
        return render(request, "appseguros/resultadoBusquedaTarea.html", {"titulo": titulo, "tareas": tareas})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)





#SINIESTROS
#mostramos todos los siniestros
def siniestros(request):
    siniestros = Siniestro.objects.all()  # Obtiene todos los Siniestros
    return render(request, 'appseguros/siniestro.html', {'siniestros': siniestros})


#Formulario de siniestros para agregar a la base de datos
def siniestroFormulario (request):
    if request.method == "POST":
        mi_formulario = SiniestroFormulario(request.POST) #Aca llega la info del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            siniestro = Siniestro(numero_siniestro=informacion["numero_siniestro"], asegurado=informacion["asegurado"], informacion=informacion["informacion"])
            siniestro.save()
            
            return redirect('siniestros') 
    else:
        mi_formulario = SiniestroFormulario()
    
    return render(request, "appseguros/siniestroFormulario.html", {"mi_formulario": mi_formulario})


#muestra resultado de la busqueda de siniestros
def resultadoBusquedaSiniestro(request):
    if "asegurado" in request.GET:
        asegurado = request.GET["asegurado"]
        siniestros = Siniestro.objects.filter(asegurado__icontains=asegurado)  
        
        return render(request, "appseguros/resultadoBusquedaSiniestro.html", {"asegurado": asegurado, "siniestros": siniestros})
    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)