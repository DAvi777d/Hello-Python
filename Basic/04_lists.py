# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_list = list()
my_other_list = []


# Acceso a elementos y búsqueda

my_list = [35,24,62,52,30,30,17]

print(my_list)
print(len(my_list))

my_other_list =[24,1.65,"Julian","Barrera"]

print(my_other_list[1])
print(my_other_list[-1]) 
print(type(my_other_list))
print(my_list.count(30)) #cuenta elementos repetidos de la misma lista
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Barrera"))

age, height, name, surname = my_other_list
print(name,surname)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list) Arroja un error

# Creación, inserción, actualización y eliminación

my_other_list.append("Dav7dd")#agrega un elemento al final
print(my_other_list)

my_other_list.insert(6, "Azul")#grega un elemento en el indicie que le indicamos
print(my_other_list)

my_other_list.insert(5,"developer")
print(my_other_list)

my_other_list[1] = "Azul"#agregamos el elemento al indice mencionado y se elimina la variable anterior
print(my_other_list)

my_other_list.remove("Azul")# elimina el primer elemento que coincida con lo que quermos eliminar
print(my_other_list)

my_list.remove(30)
print(my_list)

my_ultimo_elemento = my_list.pop### debemos guardar el elemento en alguna variable para que no se muestre por consola ###
##print(my_list.pop(1))#elimina el ultimo elemento de una lista 
print(my_list)

my_pop_element = my_list.pop(2)
#print(my_pop_element) ---el pop lo usamos para sacar el elemento y tenerlo guardado en ota lista--
print(my_list)

del my_list[2] # elimina el elemento del indice por completo
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()# copiamos nuestra anterior lista y aun si borramos la lista anterior 
# nuestra nueva lista aparecera con los mismos valores de la lista copiada

my_list.clear() # elimina todos los elementos
print(my_list)

print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # ordena la lista
print(my_new_list)

# Sublistas

print(my_new_list[1:3]) # mostrara los elementos que estan entre el uno y dos es decir 24 y 30 no toma el indice 3 si no los que estan entre 1-3

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
