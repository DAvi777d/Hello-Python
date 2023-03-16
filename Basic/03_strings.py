# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea\ndos veces"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age, lenguaje = "Julian", "Barrera", 24, "español"
hermanos, mascotas, madre = "leonardo, betty y topo", str(2), "blanca" 
print("Mi nombre es %s mi apellido %s y mi edad %d" % (name, surname, age))
print("Mi nombre es %s me apellido %s y mi edad es %d" % (name, surname, age))
print("tengo tres hermanos {}  y {} mascotas y mi madre se llama {}" .format(hermanos,mascotas,madre))
print(type(mascotas))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age) + " " + "hablo " + lenguaje)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
print(f"tengo tres hermanos {hermanos}, {mascotas} mascotas, mi madre se llama {madre} y tengo {age} años")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)



# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())#letra capital primer letra mayuscula
print(language.upper())#coloca todo el string en mayuscula
print(language.count("o"))#cuenta cuantos caracteres del argumento que pasamos tiene el string
print(language.isnumeric())#dice si es numerico o no 
print("1".isnumeric())#dice si es numerico o no
print(language.lower())#coloca todo en minusculas
print(language.lower().isupper())
print(language.startswith("Py"))#con lo que inicia el parametro que estamos usando
print("Py" == "py")  # No es lo mismo
