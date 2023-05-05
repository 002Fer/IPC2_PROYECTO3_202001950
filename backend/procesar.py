import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import re
import os
from io import BytesIO


def ObtenerListadePalabras(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\b\d+\b', '', text)
    words = text.lower().split()
    words =EliminarPalabras(words)
    return words

def EliminarPalabras(lista):
    ruta_archivo = 'diccionario.xml'
    if os.path.exists(ruta_archivo):
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        xml_string = ET.tostring(root, encoding='utf8', method='xml').decode('utf8')
        diccionario1=xmlADiccionario(xml_string)
        Listaeliminar=diccionario1['eliminar']
        for palabra in lista:
            if palabra.lower() in [eliminar.lower() for eliminar in Listaeliminar]:
                lista.remove(palabra)
        return lista
    return lista

def xmlADiccionario(xml_string):
    root = ET.fromstring(xml_string)
    result_dict = {}
    for categoria in root.findall('perfil'):
        nombre = categoria.find('nombre').text
        palabras = [p.text for p in categoria.findall('palabrasClave/palabra')]
        result_dict[nombre] = palabras
    return result_dict

def xmlUsuario(xml_string):
    root = ET.fromstring(xml_string)
    result_nom = {}
    for categoria in root.findall('perfiles'):
        nombre = categoria.find('nombre').text
        palabras = [p.text for p in categoria.findall('perfil/nombre')]
        result_nom[nombre] = palabras
    return result_nom

def unificarDiccionarios(diccionario1, diccionario2):
    keys = set(diccionario1.keys()).union(set(diccionario2.keys()))
    nuevo_diccionario = {}
    for key in keys:
        valores1 = set(diccionario1.get(key, []))
        valores2 = set(diccionario2.get(key, []))
        nuevo_diccionario[key] = list(valores1.union(valores2))
    return nuevo_diccionario

def EscribirBasePalabras(datos):
    root = ET.Element('categorias')
    for key, value in datos.items():
        head=SubElement(root,'categoria')
        ET.SubElement(head, 'nombre').text=key
        elemento=SubElement(head,'palabras')
        for item in value:
            ET.SubElement(elemento, 'palabra').text = item
    tree = ET.ElementTree(root)
    tree.write('diccionario.xml', encoding='utf-8', xml_declaration=True)