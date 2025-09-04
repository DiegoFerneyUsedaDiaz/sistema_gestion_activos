from django.db import models

# Create your models here.
class Tipo_activo(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
        
class Ubicacion(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
            
class Estado(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
         return self.nombre
            
class Empleado(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    area= models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Activos(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    fecha_adquisicion = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    Tipo_activo = models.ForeignKey('Tipo_activo', on_delete=models.CASCADE)
    Ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    Estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    Empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

