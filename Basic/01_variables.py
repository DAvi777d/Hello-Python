# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable =str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable)) 

my_bool_variable = False
print(my_bool_variable)

#concatenacion de variables en un print
print(my_string_variable,my_int_variable, my_bool_variable)
print("este es el valor de:", my_bool_variable)

#Algunas funciones del sistema 
print(len(my_string_variable)) # la funcion len cuenta los elementos

#Variables en una sola linea
name, surname, alias, edad = "Julian", "Barrera", "Mono", 24
print("*Mi nombre es:",name,"*Mi apellido es:", surname,"*Mi alias es:", alias,"*Mi edad es:", edad)

# Inputs
first_name = input("what is your name?:")
age = input("how old are you?:")

print(first_name)
print(age)
