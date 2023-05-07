import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import re
import os
from io import BytesIO


perfilesclave={}
lista=[]
lista_ignorar=[]

mensajes=[]
def ProcessData(xml):
    if xml:
        doc=ET.fromstring(xml)
        perfiles=doc.findall('perfiles')
        descartadas=doc.find('descartadas')

        for descartar in descartadas:
            palabradescartar=descartar.text
            lista_ignorar.append(palabradescartar)
    
    
        
        for perfil in perfiles:
            perfil1=perfil.findall('perfil')
            for perfil2 in perfil1:
                nomlista=perfil2.find('nombre').text
                nom=perfil2.find('nombre').text
                nomlista=list()
                palabrasClave=perfil2.find('palabrasClave')
                for palabra in palabrasClave:
                    nombreper=palabra.text
                    nomlista.append(palabra.text)
                perfilesclave[nom]=nomlista
        print(perfilesclave)
        print(descartadas)


def ProceData(xml2):
    if xml2:
        doc=ET.fromstring(xml2)
        mensajes=doc.findall('mensaje')

        for descartar in mensajes:
            palabra=descartar.text
            mensajes.append(palabra)
        print(mensajes)


def ObtenerListadePalabras(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\b\d+\b', '', text)
    words = text.lower().split()
    words =EliminarPalabras(words)
    return words

def EliminarPalabras(lista):
    Listaeliminar=lista_ignorar
    for palabra in lista:
        if palabra.lower() in [eliminar.lower() for eliminar in Listaeliminar]:
            lista.remove(palabra)
    return lista


def ObtenerProcentajesDeGeneros(listaPalabras,artista):
    totalPalabras=len(listaPalabras)
    root=Element('respuesta')
    SubElement(root,'artista').text=artista
    SubElement(root,'totalpalabras').text=str(totalPalabras)
    categorias=SubElement(root,'categorias')
    
    
    coincidencias=0
    for genero, palabrasgenero in perfilesclave.items():
        if genero!=None:
            coincidencias=0
            for palabra in listaPalabras:
                if palabra.lower() in [p.lower() for p in palabrasgenero]:
                    coincidencias+=1
            categoria=SubElement(categorias,'categoria')
            SubElement(categoria,'nombre').text=genero
            SubElement(categoria,'coincidencias').text=str(coincidencias)
            SubElement(categoria,'porcentaje').text=str((coincidencias/totalPalabras)*100)
    tree = ElementTree(root)
    xml_data = BytesIO()
    xml_bytes = tree.write(xml_data,encoding='UTF-8', xml_declaration=True)
    return xml_data.getvalue()