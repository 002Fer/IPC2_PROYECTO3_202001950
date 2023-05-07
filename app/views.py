
from django.shortcuts import render
from django.http import HttpResponse
import requests
import xml.etree.ElementTree as ET

# Create your views here.
def Welcome(request):
    r = requests.get('http://127.0.0.1:5000/')
    print( r.json()) 
    respuesta = r.json()
    return HttpResponse("<h1>Welcome msg = "+respuesta['MSG']+"</h1>")

def mis_datos(request):
    
    return render(request,'datos.html')

def perfil(request):
    if request.method=='POST':
        archivo=request.FILES['file']
        
        #headers={'content-Type': "aplicacion/xml"}
        response = requests.post('http://127.0.0.1:5000/analizar', data=archivo)

        if response.status_code==200:
            xml=response.content.decode("utf-8")
            print(str(xml))
            respuesta="Se cargo con exito el archivo "+ xml
            return render(request,'ocupacion.html',{'respuesta':respuesta})
    else:
        return render(request,'ocupacion.html')
    
def mensajes(request):
    if request.method=='POST':
        entrada=request.FILE['entrada']

        response=requests.post('http://127.0.0.1:5000/mostrar',data=entrada)

        if response.status_code==200:
            xml=response.content.decode("utf-8")
            print(str(xml))
            respuesta_2=xml
            return render(request,'texto.html',{'respuesta':respuesta_2})



