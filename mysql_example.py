import mysql.connector
from mysql.connector import errorcode


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print "Failed creating database: {}".format(err)
        exit(1)



config = {
  'user': 'root',
  'password': 'Cic1234*',
  'host': '127.0.0.1',
# 'database': 'university',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)
cursor.execute("drop database example")
cnx.commit()
DB_NAME = 'example'
TABLES = {}
TABLES['alumnos'] = (
    "CREATE TABLE alumnos ("
    "  alumno_id int(11) NOT NULL,"
    "  Nombre varchar(30) NOT NULL,"
    "  ApellidoP varchar(30) NOT NULL,"
    "  ApellidoM varchar(30) NOT NULL,"
    "  Creditos int(11) NOT NULL,"
    "  PRIMARY KEY (alumno_id)"
    ") ENGINE=InnoDB")

TABLES['materias'] = (
   "CREATE TABLE materias ("
   " materia_id int(11) NOT NULL,"
   " depto_name varchar(30) NOT NULL,"
   " Creditos int(11) NOT NULL,"
   " PRIMARY KEY (materia_id)"
   ") ENGINE=InnoDB")

TABLES['profesores'] = (
  "CREATE TABLE profesores ("
  "profesor_id int(11) NOT NULL,"
  "depto_name varchar(30) NOT NULL,"
  "academia_id int(11) NOT NULL,"
  "Nombre varchar(30) NOT NULL,"
  "ApellidoP varchar(30) NOT NULL,"
  "ApellidoM varchar(30) NOT NULL,"
  "PRIMARY KEY (profesor_id)"
 # "FOREIGN KEY (academia_id) references academia"
  ") ENGINE=InnoDB")

TABLES['academias'] = (
   "CREATE TABLE academias ("
   "nombre varchar(30) NOT NULL,"
   "academia_id int(11) NOT NULL,"
   "plantel varchar(30) NOT NULL,"
   "PRIMARY KEY(academia_id)" 
   ")  ENGINE=InnoDB")

TABLES['egresados'] = (
   "CREATE TABLE egresados ("
    "alumno_id int(11) NOT NULL,"
    "Nombre varchar(30) NOT NULL,"
    "ApellidoP varchar(30) NOT NULL,"
    "ApellidoM varchar(30) NOT NULL,"
    "Generacion int(6) NOT NULL,"
    "PRIMARY KEY (alumno_id)"
   ")  ENGINE=InnoDB")

TABLES['asistentes'] = (
   "CREATE TABLE asistentes("
   "trabajador_id int(11) NOT NULL,"
   "academia_id int(11) NOT NULL," 
   "Nombre varchar(30) NOT NULL,"
   "ApellidoP varchar(30) NOT NULL,"
   "ApellidoM varchar(30) NOT NULL,"
   "PRIMARY KEY (trabajador_id)"
#   "FOREIGN KEY (academia_id) references academias"
 ") ENGINE=InnoDB")




try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print err
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print "Creating table {}: ".format(name)
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print "already exists."
        else:
            print err.msg
    else:
        print "OK"


add_materia = ("INSERT INTO materias (materia_id, depto_name, Creditos) VALUES (%(materia_id)s, %(depto_name)s, %(Creditos)s)")
data_materia = [
	{
	'materia_id' : 110,
	'depto_name' : 'Matematicas',
	'Creditos' : 10
	},
	{
	'materia_id' : 112,
	'depto_name' : 'Administracion',
	'Creditos' : 20
	},
        {
         'materia_id' : 113,
         'depto_name' : 'Administracion',
         'Creditos'    : 10
        },
]

add_academia = ("INSERT INTO academias (nombre, academia_id, plantel) VALUES (%(nombre)s, %(academia_id)s, %(plantel)s) ")
data_academia = [
	{ 
	 'nombre' : 'Matematicas',
         'academia_id' : 1200,
         'plantel' : 'Coyoacan'
	},
	{
	'nombre' : 'Fisica',
 	'academia_id' : 101,
        'plantel' : 'Zacatenco'
	},
	{
	'nombre' : 'Administracion',
	'academia_id' : 1300,
	'plantel' : 'Coyoacan'
	}
]

add_profesores = ("INSERT INTO profesores (profesor_id, depto_name, academia_id, Nombre, ApellidoP, ApellidoM) VALUES (%(profesor_id)s, %(depto_name)s, %(academia_id)s, %(Nombre)s, %(ApellidoP)s, %(ApellidoM)s) ")
data_profesores = [
	{
	'profesor_id' : 123,
  	'depto_name'  : 'Matematicas',
	'academia_id' : 1200,
  	'Nombre'      : 'Raul',
	'ApellidoP'   : 'Vallejo',
 	'ApellidoM'   : 'Garcia'
	},
	{
	'profesor_id' : 345,
	'depto_name'  : 'Fisica',
	'academia_id' : 101,
	'Nombre'      : 'Augusto',
	'ApellidoP'   : 'Lopez',
	'ApellidoM'   : 'Wario', 
	},
	{
	'profesor_id' : 666,
	'depto_name'  : 'Administracion',
	'academia_id' : 1300,
	'Nombre'      : 'Raul',
	'ApellidoP'   : 'Duenias',
	'ApellidoM'   : 'Munioz' 
	},
]

add_egresados = ("INSERT INTO egresados (alumno_id, Nombre, ApellidoP, ApellidoM, Generacion) VALUES ( %(alumno_id)s, %(Nombre)s, %(ApellidoP)s, %(ApellidoM)s, %(Generacion)s )")
data_egresados = [
      {
	'alumno_id' : 9805,
	'Nombre'    : 'Jose',
	'ApellidoP' : 'Vazquez',
	'ApellidoM' : 'Vazquez',
	'Generacion' : 2009	
	},
      { 
	'alumno_id' : 1544,
	'Nombre'    : 'Alfredo',
        'ApellidoP' : 'Lemus',
        'ApellidoM' : 'Rodriguez',
	'Generacion': 2010 
	},
      {
	'alumno_id' : 4127,
	'Nombre'    : 'Kenya',
	'ApellidoP' : 'Mondragon',
        'ApellidoM' : 'Velazquez',
	'Generacion': 2005
	}
]

add_asistentes = ("INSERT INTO asistentes (trabajador_id, academia_id, nombre, apellidoP, apellidoM) VALUES (%(trabajador_id)s, %(academia_id)s, %(nombre)s, %(apellidoP)s, %(apellidoM)s)")
data_asistentes = [
	{
	'trabajador_id' : 1234,
	'academia_id'   : 101,
	'nombre'	: 'Aaron',
	'apellidoP'	: 'Aparicio',
	'apellidoM'	: 'Sanchez'
	},
	{
	'trabajador_id' : 2546,
 	'academia_id'	: 1200,
	'nombre'	: 'Gabriel',
	'apellidoP'	: 'Zenon',
	'apellidoM'	: 'Leal'
	},
	{
	'trabajador_id'  : 3333,
	'academia_id'	: 1300,
	'nombre'	: 'Eliseo',
	'apellidoP'	: 'Sarmiento',
	'apellidoM'	: 'Rosales'
	}
]

for row in range(0,len(data_materia)):
	cursor.execute(add_materia,data_materia[row])
cnx.commit()

for row in range(0,len(data_academia)):
	cursor.execute(add_academia,data_academia[row])
cnx.commit()

for row in range(0,len(data_profesores)):
	cursor.execute(add_profesores,data_profesores[row])
cnx.commit()

for row in range(0,len(data_egresados)):
	cursor.execute(add_egresados,data_egresados[row])
cnx.commit()

for row in range(0,len(data_asistentes)):
	cursor.execute(add_asistentes,data_asistentes[row])
cnx.commit()

#query = ("SELECT * from alumnos where alumno_id=1")
#cursor.execute(query)
#for row in cursor:
#	print row
#update_creditos = ("UPDATE alumnos SET Creditos = %s WHERE alumno_id = %s")
#nuevo_credito={
#	'Creditos' : 10,
#	'alumno_id' : 1
#}
#cursor.execute(update_creditos,(nuevo_credito['Creditos'],nuevo_credito['alumno_id']))
#cnx.commit()
#query = ("SELECT * from alumnos where alumno_id=1")
#cursor.execute(query)
#for row in cursor:
#	print row
cursor.close()
cnx.close()
