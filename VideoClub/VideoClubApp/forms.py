from django import forms
from .models import TipoArticulo
from .models import Genero
from .models import Idioma
from .models import Articulo
from .models import Cliente
from .models import Empleado
from .models import Renta

class TipoArticuloForm(forms.ModelForm):
    class Meta:
        model = TipoArticulo
        fields = ['descripcion', 'estado']

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['descripcion', 'estado']

class IdiomaForm(forms.ModelForm):
    class Meta:
        model = Idioma
        fields = ['descripcion', 'estado']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = [
            'titulo',
            'tipo_articulo',
            'idioma',
            'renta_x_dia',
            'dias_renta',
            'monto_entrega_tardia',
            'estado'
        ]

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'cedula',
            'tarjeta_credito',
            'limite_credito',
            'tipo_persona',
            'estado'
        ]

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'cedula',
            'tanda_labor',
            'porciento_comision',
            'fecha_ingreso',
            'estado'
        ]

class RentaForm(forms.ModelForm):
    class Meta:
        model = Renta
        fields = [
            'empleado',
            'articulo',
            'cliente',
            'fecha_renta',
            'fecha_devolucion',
            'monto_x_dia',
            'cantidad_dias',
            'comentario',
            'estado'
        ]