##############################################
# CREAR UNA BASE DE DATOS

from pymongo import MongoClient
    
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = 'mongodb+srv://tomas:tomas@cluster.bco8el6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster'
 
   # Crear una conexión usando MongoClient. Puedes importar MongoClient o usar pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Crear la base de datos para nuestro ejemplo (utilizaremos la misma base de datos durante todo el tutorial
   return client['user_shopping_list']
  
# Esto se añade para que muchos archivos puedan reutilizar la función get_database()
if __name__ == "__main__":   
  
   # Obtener la base de datos
    dbname = get_database()

# -------------------------------------------------------------------------------------------------------------------------
# MongoDB no crea una base de datos hasta que tienes colecciones y documentos en ella. Así que vamos a crear una colección.
# -------------------------------------------------------------------------------------------------------------------------