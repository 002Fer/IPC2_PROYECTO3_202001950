import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import re
import os
from io import BytesIO


perfilesclave={}
lista=[]
lista_ignorar=[]
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