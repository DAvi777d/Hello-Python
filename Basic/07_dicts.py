# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Julian",
                 "Apellido": "Barrera", "Edad": 24, 1: "Python"}

my_dict = {
    "Nombre": "Julian",
    "Apellido": "Barrera",
    "Edad": 24,
    "Lenguajes": {"Python", "javascript", "Kotlin"},
    1: 1.65
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Julian" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle MoureDev"#agregamos un nuevo valor y clave
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"# actualiza el valor de la clave nombre 
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items()) #listado de todos los items separados con valores por ()
print(my_dict.keys())#muestra las claves 
print(my_dict.values())# muestra todos los valores
#print(my_dict.fromkeys("Nombre",1))#crea un diccionario en base al anterior 

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)#creamos un nuevo diccionario con las claves del diccionario anterior
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")#crea un diccionario con un valor 
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))
