from .auxiliares import obtener_maximo, promedio, obtener_mitad_de_maximo, quick_sort, bubble_sort, selection_sort


def utn_mostrar_nombres_heroes(lista_nombres:list)->None:
    """recibe una lista de nombres y los muestra
    Args:
        lista_nombres (list): lista de nombres
    """
    for nombre in lista_nombres:
        print (nombre)

def utn_mostrar_identidades_heroes(lista_identidades:list)->None:
    """ recibe una lista con identidades y las muestra.

    Args:
        lista_identitdades (list): lista de identidades.
    """

    for identidades in lista_identidades:
        print(identidades)

def utn_mostrar_mayor_altura (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    """ Recibe cinco listas y muestra los datos del heroe mas alto.

    Args:
        nombres (list): lista de nombres
        identidades (list): lista de identidades
        generos (list): lista de generos
        poderes (list): lista de poderes
        alturas (list): lista de alturas
    """
    maximo = obtener_maximo (alturas)
    for indice in range(len(alturas)):
        if alturas[indice] == maximo:
            mensaje = f"nombre: {nombres[indice]} | identidad: {identidades[indice]} | genero: {generos[indice]} | poder: {poderes[indice]} | altura: {alturas[indice]}"
            print (mensaje)

def utn_mostrar_heroes_mas_fuertes (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    """
    Recibe cinco listas y muestra a los heroes mas fuertes
    Args:
        nombres (list): lista de nombres
        identidades (list): lista de identidades
        generos (list): lista de generos
        poderes (list): lista de poderes
        alturas (list): lista de alturas
    """
    mas_fuerte = obtener_maximo(poderes)
    for indice in range(len(poderes)):
        if poderes[indice] == mas_fuerte:
            mensaje = f"nombre: {nombres[indice]} |     identidad: {identidades[indice]} |    genero: {generos[indice]} |    poder: {poderes[indice]} |    altura: {alturas[indice]}"
            print (mensaje)

#FALTA DOCUMENTAR
def utn_filtrar_heroes_genero (nombres: list, identidades: list, generos: list, poderes:list, alturas:list, genero_buscado: str)->None:

    
    for indice in range(len(generos)):
        if generos[indice]== genero_buscado:
            mensaje = f"nombre: {nombres[indice]} |     identidad: {identidades[indice]} |    genero: {generos[indice]} |    poder: {poderes[indice]} |    altura: {alturas[indice]}"
            print (mensaje)

def utn_mostrar_heroes_poder_superior_promedio (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    poder_promedio = promedio(poderes)
    for indice in range(len(poderes)):
        if poderes[indice] > poder_promedio:
            mensaje = f"nombre: {nombres[indice]} |  identidad: {identidades[indice]} |   genero: {generos[indice]} |    poder: {poderes[indice]} |    altura: {alturas[indice]}"
            print (mensaje)

def utn_mostrar_heroes_mas_debiles(nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    mitad_maximo = obtener_mitad_de_maximo(poderes)
    for indice in range(len(poderes)):
        if poderes[indice]<= mitad_maximo:
            mensaje = f"nombre: {nombres[indice]} |  identidad: {identidades[indice]} |   genero: {generos[indice]} |    poder: {poderes[indice]} |    altura: {alturas[indice]}"
            print (mensaje)

#FUNCIONES CON ORDENAMIENTO(corregir)

def utn_mostrar_heroes_poder_ascendente (poderes: list, nombres:list):
    bubble_sort (nombres, poderes)
    for indice in range(len(poderes)):
            print (f"Nombre : {nombres[indice]} | poder: {poderes[indice]}")

def utn_mostrar_heroes_altura_descendente (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    pass
def utn_mostrar_heroes_asc_o_des (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)->None:
    pass