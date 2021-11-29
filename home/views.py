from django.shortcuts import render
from .models import tessiu
from .forms import registroTessiu
from django.shortcuts import redirect
import math
import random

# Create your views here.
def home(request):
    diccionario={}
    return render(request, "home/home.html",diccionario)

def ProcesaLista(lista,umbral=2.0):
    if umbral == None:
        umbral=random.randrange(5,60)
    listaF=[]
    for i in lista:
        distancia=math.sqrt(i.temperature**2+i.color**2)
        if distancia <= umbral:
            listaF.append(i)
        print(distancia)
    return listaF


def crearGrafo(request):
    print(request.GET)
    umbral=request.GET.get('umbral')
    print(umbral)
    Lista = tessiu.objects.get_queryset()
    L1=ProcesaLista(Lista,umbral)
    diccionario={"lista":L1}
    return render(request, "grafo/sintactico.html",diccionario)

def registrar(request):

    data = {
        'form':registroTessiu
    }
    if request.method == 'POST':
        form = registroTessiu(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='home')
        else:
            print(form)
    return render(request,'formulario/registro.html', data)
