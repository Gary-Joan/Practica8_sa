import os
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from json import loads, dumps
from bson import json_util
# conexion a la base de datos de mongodb
app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.prueba
mycol= db.test
# ruta de inicio de la aplicacion
@app.route('/')
def home():
   return "<h2>API SERVIDOR A</h2>"



#ruta para verficiar los items dentro de la base de datos
@app.route('/items')
def items():
   
    _items = mycol.find()
    items = [item for item in _items]
    lista = dumps(items, default=str)
    return lista
#ruta para crear un nuevo item utilizando el metodo post  
@app.route('/new', methods=['POST'])
def new():
    data = request.get_json()
    #print(data['autor'],flush=True)
    item_doc = {
        "autor": data['autor'],
        "nota": data['nota']
    } 
    x = mycol.insert_one(item_doc)
    return str(x.inserted_id)
#ruta para ver el numero de items dentro de la coleccion de la base de datos.    
@app.route('/count')
def contador():
    _items = mycol.find()
    items_count={"cantidad ": _items.count()}
    return dumps(items_count)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80, debug=True)
