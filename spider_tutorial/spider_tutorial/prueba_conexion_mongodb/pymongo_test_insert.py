# CREAR UNA BASE DE DATOS

# Obtener la base de datos usando el método que definimos en el archivo pymongo_get_database
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["user_1_items"]