from flask import Flask,request,jsonify

from procesar import xmlADiccionario,EscribirBasePalabras,unificarDiccionarios
import xml.etree.ElementTree as ET
import os 

app = Flask(__name__)
app.config['DEBUG'] = True
print("Iniciando el servidor en el puerto por defecto 5000")

@app.route("/")
def hello_world():
    return jsonify({"MSG":"Hola a todos esto es de parte de flask"})  
#Ejemplo
#http://localhost:5000/UsuarioConectado?nombreUser=Oscar Leon
@app.route("/UsuarioConectado",methods=['GET'])
def UsuarioConectado():
    nombreUser = request.args.get('nombreUser')
    return jsonify({"Nombre":nombreUser})  


@app.route("/ObtenerDatos",methods=['POST'])
def ObtenerDatos():
    perfil = request.get_json()
    print(perfil)
    if perfil["id"]==1:

        return jsonify({"MSG":"Usuario bloqueado, Juan debe dinero"})  
    return jsonify({"MSG":"Tu si puedes pasar"}) 

#---------------------------------------------------------------------------------------

@app.route("/cargarPalabras",methods=['POST'])
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