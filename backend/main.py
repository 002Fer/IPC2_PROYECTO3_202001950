from flask import Flask,request,jsonify,Response
from procesar import ProcessData, ProceData

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"MSG":"Hola a todos esto es de parte de flask"})  

@app.route('/analizar',methods=['POST'])
def analizar():
    if request.method=='POST':
        return Response(ProcessData(request.data),status=200)

@app.route("/mostrar",methods=['POST'])
def mostrar():
    if request.method=='POST':
        return Response(ProceData(request.data),status=200)
    
if __name__=='main':
    app.run(debug=True)