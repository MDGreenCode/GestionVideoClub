from django.shortcuts import render, redirect, get_object_or_404
from .models import TipoArticulo
from .forms import TipoArticuloForm
from .models import Genero
from .forms import GeneroForm
from .models import Idioma
from .forms import IdiomaForm
from .models import Articulo
from .forms import ArticuloForm
from .models import Cliente
from .forms import ClienteForm
from .models import Empleado
from .forms import EmpleadoForm
from .models import Renta
from .forms import RentaForm

def inicio(request):
    return render(request, 'inicio.html')

def lista_tipos(request):
    tipos = TipoArticulo.objects.all()
    return render(request, 'tipos/lista.html', {'tipos': tipos})


def crear_tipo(request):
    form = TipoArticuloForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_tipos')

    return render(request, 'tipos/form.html', {'form': form})


def editar_tipo(request, id):
    tipo = get_object_or_404(TipoArticulo, id=id)
    form = TipoArticuloForm(request.POST or None, instance=tipo)

    if form.is_valid():
        form.save()
        return redirect('lista_tipos')

    return render(request, 'tipos/form.html', {'form': form})


def eliminar_tipo(request, id):
    tipo = get_object_or_404(TipoArticulo, id=id)
    tipo.delete()
    return redirect('lista_tipos')

def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'generos/lista.html', {'generos': generos})


def crear_genero(request):
    form = GeneroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_generos')

    return render(request, 'generos/form.html', {'form': form})


def editar_genero(request, id):
    genero = get_object_or_404(Genero, id=id)
    form = GeneroForm(request.POST or None, instance=genero)

    if form.is_valid():
        form.save()
        return redirect('lista_generos')

    return render(request, 'generos/form.html', {'form': form})


def eliminar_genero(request, id):
    genero = get_object_or_404(Genero, id=id)
    genero.delete()
    return redirect('lista_generos')

def lista_idiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, 'idiomas/lista.html', {'idiomas': idiomas})


def crear_idioma(request):
    form = IdiomaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_idiomas')

    return render(request, 'idiomas/form.html', {'form': form})


def editar_idioma(request, id):
    idioma = get_object_or_404(Idioma, id=id)
    form = IdiomaForm(request.POST or None, instance=idioma)

    if form.is_valid():
        form.save()
        return redirect('lista_idiomas')

    return render(request, 'idiomas/form.html', {'form': form})


def eliminar_idioma(request, id):
    idioma = get_object_or_404(Idioma, id=id)
    idioma.delete()
    return redirect('lista_idiomas')

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulos/lista.html', {'articulos': articulos})


def crear_articulo(request):
    form = ArticuloForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_articulos')

    return render(request, 'articulos/form.html', {'form': form})


def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    form = ArticuloForm(request.POST or None, instance=articulo)

    if form.is_valid():
        form.save()
        return redirect('lista_articulos')

    return render(request, 'articulos/form.html', {'form': form})


def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    articulo.delete()
    return redirect('lista_articulos')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})


def crear_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'clientes/form.html', {'form': form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)

    if form.is_valid():
        form.save()
        return redirect('lista_clientes')

    return render(request, 'clientes/form.html', {'form': form})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('lista_clientes')

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})


def crear_empleado(request):
    form = EmpleadoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_empleados')

    return render(request, 'empleados/form.html', {'form': form})


def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    form = EmpleadoForm(request.POST or None, instance=empleado)

    if form.is_valid():
        form.save()
        return redirect('lista_empleados')

    return render(request, 'empleados/form.html', {'form': form})


def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('lista_empleados')

def lista_rentas(request):
    rentas = Renta.objects.all()
    return render(request, 'rentas/lista.html', {'rentas': rentas})


def crear_renta(request):
    form = RentaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_rentas')

    return render(request, 'rentas/form.html', {'form': form})


def editar_renta(request, id):
    renta = get_object_or_404(Renta, id=id)
    form = RentaForm(request.POST or None, instance=renta)

    if form.is_valid():
        form.save()
        return redirect('lista_rentas')

    return render(request, 'rentas/form.html', {'form': form})


def eliminar_renta(request, id):
    renta = get_object_or_404(Renta, id=id)
    renta.delete()
    return redirect('lista_rentas')