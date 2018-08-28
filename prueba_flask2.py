#Importamos modulos
from flask import Flask, jsonify, request
import json
import csv

'''
Tarea
1. Leer el archivo  "TodasLasNoticias.csv" y pasarlo
a un archivo JSON. El objeto contendrá una lista con
un diccionario por cada posición, donde cada diccionario
tendrá cinco llaves:
I Fecha
II Título
III url
IV Descripción
V Categoría
'''
#C:\Users\user\.PyCharmCE2018.2\config\scratches\prueba_flask2.py
'''
with open('.\TodasLasNoticias.csv','r', encoding = 'utf-8') as outfile1:
    fileReader = csv.reader(outfile1, delimiter=',', quotechar = '"' )
    print(fileReader.__sizeof__())

'''
   # numero_lin = 0
   # for row in fileReader:
   #     numero_lin +=1
   # print(numero_lin)


'''
    obj_noticias = []
    noticias = {'data': obj_noticias}
    print(fileReader.__dir__())

    i=0
    for linea in fileReader:
        if i ==0:
            print(linea)
        i=1
        if len(linea) ==5:
            obj_noticias.append({
                'Fecha'     : linea[0],
                'Titulo'    : linea[1],
                'url'       : str(linea[2]),
                'Descripcion' : linea[3],
                'Categoria' : linea[4]
            })
        elif len(linea) == 4:
            pedazo = len(linea[3].split("\","))
            if pedazo == 2:
                linea.append(linea[3].split("\",")[1])
    ### Si hay ese patron, en el que a la direccion le falta una coma
            elif pedazo ==1 and linea[1].rfind("\",http") != -1 :
                swap = tuple(linea)
                tupla = swap[1].split("\",")
                linea[0] = linea[0]
                linea[1] = tupla[0]
                linea[2] = tupla[1]
                linea[3] = swap[2]
                linea.append(swap[3])
                obj_noticias.append({
                    'Fecha': linea[0],
                    'Titulo': linea[1],
                    'url':    linea[2],
                    'Descripcion': linea[3:-1],
                    'Categoria': linea[len(linea)-1]
                })
            elif len(linea)>5:
                obj_noticias.append({
                    'Fecha': linea[0],
                    'Titulo': linea[1],
                    'url': linea[2],
                    'Descripcion': linea[3:-1],
                    'Categoria': linea[len(linea) - 1]
                })

    print(len(obj_noticias))
'''
#    with open('noticias.json', 'w') as outfile:
#        json.dump(obj_noticias, outfile)



app = Flask(__name__)

@app.route('/<categoria>')
def imprime(categoria):
    with open('noticias.json', 'r', encoding="utf-8") as jfile1 :
        data_news = json.load(jfile1)

    return data_news[0]['categoria']

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug = True )