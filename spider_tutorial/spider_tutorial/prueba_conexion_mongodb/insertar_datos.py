# INSERTAR DATOS EN LA BASE DE DATOS
# Este es el archivo que se debe ejecutar (pymongo_get_database y pymongo_test_insert no se ejecutan)

from pymongo_test_insert import collection_name, dbname

item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])