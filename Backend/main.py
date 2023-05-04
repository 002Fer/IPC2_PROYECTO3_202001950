from flask import Flask,request,Response,jsonify
from proceso import xmlADiccionario,EscribirBasePalabras,unificarDiccionarios
import xml.etree.ElementTree as ET
import os 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/base'
app.config['DEBUG'] = True

@app.route("/consultarDatos",methods=['GET'])
def consulta():
    nombreUser=request.args.get('nombreUser')
    return jsonify({"nombre":nombreUser})

@app.route("/procesarSolicitud",methods=['POST'])
def Cargar():
    if request.method=='POST':
        ruta_archivo = 'diccionario.xml'
        if os.path.exists(ruta_archivo):
            tree = ET.parse(ruta_archivo)
            root = tree.getroot()
            xml_string = ET.tostring(root, encoding='utf8', method='xml').decode('utf8')
            diccionario1=xmlADiccionario(request.data)
            diccionario2=xmlADiccionario(xml_string)
            diccionarioNuevo=unificarDiccionarios(diccionario1,diccionario2)
            EscribirBasePalabras(diccionarioNuevo)
        else:
            EscribirBasePalabras(xmlADiccionario(request.data))
        return "Ok"
    else:
        return "Wrong response"

    
if __name__=='_main_':
    app.run()
        
