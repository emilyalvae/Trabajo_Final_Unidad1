import requests

def generacion():

    url_generacion="https://pokeapi.co/api/v2/generation/"

    lista_generacion=["1","2","3","4","5","6","7","8"]

    generacion_elegida=input("Ingrese la generación (1 al 8): ")

    while generacion_elegida not in lista_generacion:
        generacion_elegida= input("Ingrese UNA GENERACION VALIDA de pokemon: ")

    url_generacion_elegida=url_generacion + generacion_elegida


    pass

def forma():

    
    url_forma="https://pokeapi.co/api/v2/pokemon-shape/"
    response= requests.get(url_forma)
    datos=response.json() 

    lista_forma=[]
    for i in datos["results"]:
        lista_forma.append(i["name"])

    print("-----------LISTA DE FORMAS DE POKEMON------------")
    print(lista_forma)  


    pokemon_shape= input("Ingrese LA FORMA de pokemon: ")

    while pokemon_shape not in lista_forma:
        pokemon_shape= input("Ingrese UNA FORMA VALIDA de pokemon: ")

    pokemon_url=url_forma + pokemon_shape





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

