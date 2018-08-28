import pandas as pd
import csv
from datetime import datetime
from dateutil.parser import parse


#########################
# Leer el archivo de velocidades.csv
#######################
'''
Cargar los datos a un data frame y responder a las siguientes preguntas:
a. ¿Cuántos registros tiene la base de datos?
b. ¿Cuántos vehículos existen en la base de datos?
c. ¿Cuantos dias aparecen, y de que fecha a que fecha son los registros?
d. ¿Cuántos meses completos de información se tienen?
e. ¿En qué horario trabaja la flota?
f. ¿Cuál es la velocidad máxima registrada y que vehículo es?
g. El límite de velocidad máximo permitido es de 80 Km/h, ¿Cuántos vehículos lo rebasan y
cuales son?
h. ¿Cuál es la hora con mayor frecuencia de excesos velocidad?
i. Tomando en cuenta los meses completos, ¿Cuál es la velocidad promedio de cada mes?

'''

'''
lista = []
i=0
with open('velocidades.csv', 'r', encoding="utf-8") as file1 :
    filereader = csv.reader(file1, delimiter = ',', quotechar = "'")

    for line in filereader:
        dictio = {
                    'id'    :   line[0],
                    'Vehiculo'  :   line[1],
                    'a'     : line[2],
                    'b'     : line[3],
                    'c'     : line[4],
                    'd'     : line[5],
                    'fecha' : line[6],
                    'hora'  : line[7],
                    'velocidad' : line[8]
        }
        lista.append(dictio)
print(len(lista))
del(lista)
'''
## Cuantos registros tiene la base de deatos 3,588,921
#serie1 = pd.Series( [ l['id']       for l in lista]  )
#serie2 = pd.Series( [ l['Vehiculo'] for l in lista]  )
#serie3 = pd.Series( [ l['a']        for l in lista]  )

df1 = pd.read_csv( 'velocidades.csv', sep=",", low_memory=True, names = ['id', 'vehiculo', 'a', 'b', 'c', 'd','fecha','hora','velocidad' ] )

regis    = df1['id'].count()
print(regis)
num_vehi = df1.groupby['vehiculo'].unique()
len(num_vehi)
#26
num_dias = len(df1['fecha'].unique())
#46 dias
df1['fh'] = pd.to_date(df1['fecha'])
#df1['fh'] = pd.todatetime(df1['fecha'])
    #df1 = pd.read_csv(filepath = 'velocidades.csv', sep =",", columns = ['id', 'Vehiculo', 'a', 'b', 'c','d', 'hora','velocidad'])



