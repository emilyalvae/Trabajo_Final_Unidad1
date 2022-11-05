import requests



def generacion():
    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_generacion="https://pokeapi.co/api/v2/generation/"

    lista_generacion=["1","2","3","4","5","6","7","8"]

    generacion_elegida=input("Ingrese la generación (1 al 8): ").lower()

    while generacion_elegida not in lista_generacion:
        generacion_elegida= input("Ingrese UNA GENERACION VALIDA de pokemon: ").lower()

    url_generacion_elegida = url_generacion + generacion_elegida

    response_generacion= requests.get(url_generacion_elegida)
    datos_generacion = response_generacion.json()   

    #SE LISTAN EL NOMBRE, HABILIDAD Y LINK DE LOS POKEMONES DE LA GENERACION ESCOGIDA
    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]


    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos_generacion["pokemon_species"]:
        pokemon_nombre.append(i["name"])

        pokemon=url_api_v2_pokemon + i["name"]
        response= requests.get(pokemon)
        datos=response.json()

        pokemon_habilidad_2=[]
        for y in datos["abilities"]:
            pokemon_habilidad_2.append(y["ability"]["name"])
        
        pokemon_link.append(datos["sprites"]["back_default"])
        pokemon_habilidad.append(pokemon_habilidad_2)
    
    print("A continuación se muestran los NOMBRES, HABILIDADES, link de la imagen")
    print(list(zip(lista_generacion, pokemon_habilidad, pokemon_link)))

   

def forma():

    url_api_v2_pokemon="https://pokeapi.co/api/v2/pokemon/"
    url_forma="https://pokeapi.co/api/v2/pokemon-shape/"
    response= requests.get(url_forma)
    datos=response.json() 

    lista_forma=[]
    for i in datos["results"]:
        lista_forma.append(i["name"])

    print("-----------LISTA DE FORMAS DE POKEMON------------")
    print(lista_forma)  


    forma_escogida= input("Ingrese LA FORMA de pokemon: ").lower()

    while forma_escogida not in lista_forma:
        forma_escogida= input("Ingrese UNA FORMA VALIDA de pokemon: ").lower()

    url_forma_elegida=url_forma + forma_escogida

    response= requests.get(url_forma_elegida)
    datos=response.json()   

    #SE LISTAN EL NOMBRE, HABILIDAD Y LINK DE LOS POKEMONES DE LA FORMA ESCOGIDA

    pokemon_nombre=[]
    pokemon_habilidad=[]
    pokemon_link=[]

    print("CARGANDO LOS DATOS...ESTO PUEDE TARDAR UNOS SEGUNDOS")

    for i in datos["pokemon_species"]:
        pokemon_nombre.append(i["name"])



        pokemon=url_api_v2_pokemon + i["name"]
        response= requests.get(pokemon)
        datos=response.json()

        pokemon_habilidad_2=[]
        for y in datos["abilities"]: 
            pokemon_habilidad_2.append(y["ability"]["name"])
        
        pokemon_link.append(datos["sprites"]["back_default"])
        pokemon_habilidad.append(pokemon_habilidad_2)

    print(f"TIPO: {forma_escogida}")
    print(f"A continuación se muestran los NOMBRES, HABILIDADES, link de la imagen . De todos aquellos que tienen LA FORMA de {pokemon_shape}")
    print("(NOMBRE - HABILIDADES - LINK)")
    print(list(zip(pokemon_nombre, pokemon_habilidad, pokemon_link)))




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

