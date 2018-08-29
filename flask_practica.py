#Importamos modulos
from flask import Flask, jsonify, request, Response
import json
import csv


app = Flask(__name__)

@app.route('/<categoria>')
def imprime(categoria):
    with open('C:/Users/MB68387/Documents/LPHW/noticias.json', 'r') as jfile1 :
        data_news = json.load(jfile1)

    #categor = { el['Categoria'] for el in data_news }
    #feed = [el for el in data_news if el['Categoria'] == categoria ]
        
    #if categoria in categor:
    responde = Response(json.dumps([noti for noti in data_news if noti['Categoria']==str(categoria)]), content_type = "application/json; charset=utf-8")
    return responde

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True )