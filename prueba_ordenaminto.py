from .data_heroes import lista_alturas_heroes, lista_generos_heroes, lista_identidades_heroes, lista_nombres_heroes, lista_poder_heroes


def utn_mostrar_heroes_poder_orden_asc (alturas:list,generos:list,identidades:list,nombres:list,poderes:list)->None:
    lista_ordenada = quick_sort (lista_poder)
    for indice in range(len(lista_ordenada)):
        if lista_ordenada[indice]==indice:
            mensaje = f"nombre: {nombres[indice]} |     identidad: {identidades[indice]} |    genero: {generos[indice]} |    poder: {poderes[indice]} |    altura: {alturas[indice]}"
            print (mensaje)
        
#COMENTADO ----------------------------------
#https://onlinegdb.com/dhAG7gkPO



#la lista ya tiene que venir parseada, si o si numerica
def bubble_sort (lista_numerica: list[int]):#usa dos for para comparar dos indices diferentes y tomar sus valores e intercambiar
    for indice_Uno in range(len(lista_numerica) -1): #EL BUCLE EMPIEZA EN EL INDICE 0, Y TERMINA EN EL ULTIMO -1
        for indice_Dos in range (indice_Uno + 1, len(lista_numerica)):#EMPIEZA EN EL INDICE 2 Y TERMINA EN EL ULTIMO INDICE
            if lista_numerica[indice_Uno] > lista_numerica[indice_Dos]: #COMPARO LOS VALORES DE CADA INDICE Y SI ES MAYOR...
                aux = lista_numerica[indice_Uno] #se guarda el valor del indice porque luego se pisa
                lista_numerica[indice_Uno] = lista_numerica[indice_Dos] #...INTERCAMBIA VALORES
                lista_numerica[indice_Dos] = aux


def seleccion_sort (lista_numerica:list[int]):
    for indice_Uno in range(len(lista_numerica)-1):
        indice_minimo = indice_Uno 
        for indice_Dos in range(indice_Uno + 1, len(lista_numerica)):
            if lista_numerica[indice_Dos]<lista_numerica[indice_minimo]:
                indice_minimo = indice_Dos
                
        if indice_minimo != indice_Uno:
            lista_numerica[indice_Uno], lista_numerica[indice_Dos] =  lista_numerica[indice_Dos], lista_numerica[indice_Uno]
                
        

def quick_sort (lista_numerica:list[int])-> list[int]:
    if len(lista_numerica)<2:
        return lista_numerica
    pivote = lista_numerica.pop()  #pop por default saca y devuelve solo el ultimo elemenot
    mas_chicos = [] #creamos listas vacias para agregar los elemetos q cumplas la condicion
    mas_grandes = []
    for numero in lista_numerica:
        if numero <= pivote:
            mas_chicos.append(numero) #append agrega el elemento en la lista 
        else:
            mas_grandes.append(numero)
        return quick_sort(mas_chicos) +[pivote] + quick_sort(mas_grandes) 

#funciones utn
def ordenar_manera_ascendente (lista_poderes, lista_nombres):
    lista_ordenada = quick_sort (lista_poderes)