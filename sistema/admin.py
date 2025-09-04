from django.contrib import admin

# Register your models here.
from .models import  Tipo_activo, Ubicacion, Estado, Empleado ,Activos

      
@admin.register(Tipo_activo)
class Tipo_activoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',) 
    
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'direccion')
    search_fields = ('nombre', 'direccion')
    
@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',) 
    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'cargo', 'area', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'cargo', 'area')    
    
@admin.register(Activos)
class ActivosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'modelo', 'fecha_adquisicion', 'valor', 'Tipo_activo', 'Ubicacion', 'Estado', 'Empleado')
    search_fields = ('nombre', 'marca', 'modelo')
    list_filter = ('Tipo_activo', 'Ubicacion', 'Estado')  
