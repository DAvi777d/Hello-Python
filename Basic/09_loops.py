# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=23822

### Loops ###

# While

other_condition = 0
my_condition = 0

while my_condition < 10:
    print(my_condition)
   

    my_condition += 2

else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
else: 
    print("mi condicion es igual a 10")
    

while other_condition < 20:
   
    print(other_condition)
    other_condition += 1

    if other_condition == 15:#no entra el if a trabajar con un while y else pero el else si se puede combinar
        print("Se detiene la ejecución")
        #break
    #print(other_condition)--ejecutaria esto ya que esta en el ciclo y vuelve a retomar 

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (24, 1.65, "Julian", "Barrera", "Azul")

for element in my_tuple:
    print(element)

my_set = {"Julian", "Barrera", 24}

for element in my_set:
    print(element)

my_dict = {"Nombre": "Julian", "Apellido": "Barrera", "Edad": 24, 1: "Python"}

for element in my_dict.values():#si lo colocamos asi no imprimira los valores si no que imprime la clave es decir Nombre,Apellido e.t.c
#for element in my_dict#si lo colocamos asi no imprimira los 
#valores si no que imprime la clave o llave es decir Nombre,Apellido e.t.c
     
    print(element) 
    if element == "Edad":
       break
else:
    print("El bluce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")
