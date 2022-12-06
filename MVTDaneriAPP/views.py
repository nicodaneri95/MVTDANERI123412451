from django.shortcuts import render
from models import Familia
from django.http import HttpResponse
import datetime
# Create your views here.

def familiar(request):
    famili=Familia(edad=10,nombre="Nicolas Gomez", fecha=datetime.datetime.day)
    famili.save()
    cadena=f"Familiar Agregado: Nombre{famili.nombre}, Edad: {famili.edad}, Fecha: {famili.fecha}"
    return HttpResponse(cadena)
