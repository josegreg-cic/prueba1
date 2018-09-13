#Importamos modulos
from flask import Flask, jsonify, request, Response
import json
import csv




app = Flask(__name__)


from utils import ListConverter

app.url_map.converters['list'] = ListConverter


@app.route('/<categoria>/<list:words>')
def imprime(categoria,words):
    
    with open('C:/Users/MB68387/Documents/LPHW/noticias.json', 'r') as jfile1 :
        data_news = json.load(jfile1)

    #categor = { el['Categoria'] for el in data_news }
    #keywords = wsplit
        feed = []
        
        for noti in data_news:
            centinela = 0
            for palabra in words:
                if noti['Descripcion'].find(str(palabra)) != -1:
                    centinela +=1
            if centinela == len(words):
                feed.append(noti)
        
        
    #if categoria in categor:


        responde = Response(json.dumps([noti for noti in feed if noti['Categoria']==str(categoria)]), content_type = "application/json; charset=utf-8")
    return responde

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug = True )