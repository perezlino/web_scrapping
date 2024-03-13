##############################################
# PROBAR CONEXION Y LISTAR BASES DE DATOS

from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://tomas:tomas@cluster.bco8el6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)
    