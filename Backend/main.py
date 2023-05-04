from flask import Flask,request,Response,jsonify
import xml.etree.ElementTree as ET
import os 
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/base'
app.config['DEBUG'] = True

@app.route("/consultarDatos",methods=['GET'])
def consulta():
    nombreUser=request.args.get('nombreUser')
    return jsonify({"nombre":nombreUser})


    
if __name__=='_main_':
    app.run()
        
