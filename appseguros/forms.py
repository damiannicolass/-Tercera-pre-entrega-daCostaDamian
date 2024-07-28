from django import forms

#Formulario Empleado
class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

#Formulario Asegurado
class AseguradoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=3000)
    dni = forms.IntegerField()

#Formulario vehiculos
class VehiculoFormulario(forms.Form):
    dominio = forms.CharField(max_length=7)
    año = forms.IntegerField()
    numero_motor = forms.CharField(max_length=40)

#Formulario Tarea
class TareaFormulario(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=3000)

#Formulario Siniestros
class SiniestroFormulario(forms.Form):
    numero_siniestro = forms.CharField(max_length=20)
    asegurado = forms.CharField(max_length=30)
    informacion = forms.CharField(max_length=5000)

