from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class TipoArticulo(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

class Genero(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class Idioma(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    tipo_articulo = models.ForeignKey('TipoArticulo', on_delete=models.CASCADE)
    idioma = models.ForeignKey('Idioma', on_delete=models.CASCADE)
    renta_x_dia = models.DecimalField(max_digits=10, decimal_places=2)
    dias_renta = models.IntegerField()
    monto_entrega_tardia = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Cliente(models.Model):

    TIPO_PERSONA = [
        ('F', 'Física'),
        ('J', 'Jurídica'),
    ]

    nombre = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20)
    tarjeta_credito = models.CharField(max_length=25)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):

    TANDA = [
        ('M', 'Matutina'),
        ('V', 'Vespertina'),
        ('N', 'Nocturna'),
    ]

    nombre = models.CharField(max_length=150)
    cedula = models.CharField(max_length=20)
    tanda_labor = models.CharField(max_length=1, choices=TANDA)
    porciento_comision = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_ingreso = models.DateField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Renta(models.Model):

    ESTADO = [
        ('R', 'Rentado'),
        ('D', 'Devuelto'),
    ]

    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    articulo = models.ForeignKey('Articulo', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    fecha_renta = models.DateField()
    fecha_devolucion = models.DateField()

    monto_x_dia = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_dias = models.IntegerField()

    comentario = models.TextField(blank=True)

    estado = models.CharField(max_length=1, choices=ESTADO, default='R')

    def __str__(self):
        return f"Renta {self.id}"