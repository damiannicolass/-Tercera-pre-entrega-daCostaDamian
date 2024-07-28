from django.contrib import admin

from.models import Empleado, Asegurado, Vehiculo, Tarea, Siniestro

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido")
    ordering = ("nombre","apellido")

class AseguradoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni")
    ordering = ("nombre","apellido")

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("dominio", "año")
    ordering = ("dominio","año")

class TareaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtitulo")
    ordering = ("titulo","subtitulo")

class SiniestroAdmin(admin.ModelAdmin):
    list_display = ("numero_siniestro", "asegurado")
    ordering = ("numero_siniestro","asegurado")

# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Asegurado, AseguradoAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Siniestro, SiniestroAdmin)