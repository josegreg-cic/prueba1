#Importamos modulos
from flask import Flask, jsonify, request, Response
import json
import csv


app = Flask(__name__)

@app.route('/<categoria>')
def imprime(categoria):
    with open('noticias.json', 'r', encoding="utf-8") as jfile1 :
        data_news = json.load(jfile1)

   
        
    #if categoria in categor:
    responde = Response(json.dumps([noti for noti in data_news if noti['Categoria']==str(categoria)]), content_type = "application/json; charset=utf-8")
    return responde

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True )
