import requests

def generacion():
    pass

def forma():
    pass

def habilidad():
    
    url_Habilidad="https://pokeapi.co/api/v2/ability/"

    response= requests.get(url_Habilidad)
    datos=response.json() 

    lista_Habilidad=[]

    for i in datos["results"]:
        lista_Habilidad.append(i["name"])

    print("Lista de las habilidades de los 20 primeros pokemones:")
    print(lista_Habilidad)  

def habitat():

    url_Habitat="https://pokeapi.co/api/v2/pokemon-habitat/"
    response= requests.get(url_Habitat)
    datos=response.json()    

    lista_Habitat=[]

    for i in datos["results"]:
        lista_Habitat.append(i["name"])

    print("Lista de los habitat de los pokemones:")
    print(lista_Habitat) 

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

