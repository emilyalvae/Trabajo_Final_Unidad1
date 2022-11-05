import requests

def generacion():
    pass

def forma():
    pass

def habilidad():
    pass

def habitat():
    pass

def tipo():
    pass



print("----------------------------------------------------MENU---------------------------------------------------")

print("""Opción 1: Listar pokemons por generación.
Opción 2: Listar pokemons por forma. 
Opción 3: Listar pokemons por habilidad. 
Opción 4: Listar pokemons por habitat. .
Opción 5: Listar pokemons por tipo. """)


opcion=int(input("INGRESE UNA OPCION DEL 1 AL 5: "))
opciones=[1,2,3,4,5]

while opcion not in opciones:
    opcion=int(input("INGRESE UNA OPCION VALIDA DEL 1 AL 5: "))

if opcion==1:
    generacion()
if opcion==2:
    forma()
if opcion==3:
    habilidad()
if opcion==4:
    habitat()
if opcion==5:
    tipo()

