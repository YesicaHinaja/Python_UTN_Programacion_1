# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time
from data_heroes import lista_poder_heroes

def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load(r'C:\Users\yesic.DESKTOP-63K61PJ\OneDrive\Escritorio\Python_UTN_Programacion_1\02_Desafios\Desafio_01\assets\snd\select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

#FUNCIONES DESAROLLADAS

def obtener_maximo (lista_numeros: list)-> float:
    """
    obtiene el valor maximo de los elementos de lista y lo devuelve parseado
    Args:
        lista_numeros (list): lista de numeros
    Returns:
        float: el valor maximo parseado
    """
    if not lista_numeros:
        print ("ERROR. LISTA VACIA")
        return None
    else: 
        numero_max = lista_numeros[0]
        for numero in lista_numeros:
            if numero > numero_max:
                numero_max = numero
            
        return float(numero_max)

#falta documentar
def promedio(lista_numeros: list)-> float:
    suma = 0
    cantidad = len(lista_numeros)
    for numero in lista_numeros:
        suma += numero
    
    promedio = suma / cantidad
    return promedio

def obtener_mitad_de_maximo (lista_numeros: float) ->int:
    
    maximo = obtener_maximo(lista_numeros)
    mitad = maximo / 2
    return mitad

#FUNCIONES DE ORDENAMIENTO




def bubble_sort (lista_numerica: list, lista_nombres:list)-> None:
    for indice_Uno in range(len(lista_numerica) -1): 
        for indice_Dos in range (indice_Uno + 1, len(lista_numerica)):
            if lista_numerica[indice_Uno] > lista_numerica[indice_Dos]: 
                    lista_numerica[indice_Uno], lista_numerica[indice_Dos] =\
                    lista_numerica[indice_Dos], lista_numerica[indice_Uno]

                    lista_nombres[indice_Uno], lista_nombres[indice_Dos] =\
                    lista_nombres[indice_Dos], lista_nombres[indice_Uno]




def selection_sort (lista_numerica:list[int]):
    for indice_Uno in range(len(lista_numerica)-1):
        indice_minimo = indice_Uno 
        for indice_Dos in range(indice_Uno + 1, len(lista_numerica)):
            if lista_numerica[indice_Dos]<lista_numerica[indice_minimo]:
                indice_minimo = indice_Dos
        if indice_minimo != indice_Uno:
            lista_numerica[indice_Uno], lista_numerica[indice_Dos] =  lista_numerica[indice_Dos], lista_numerica[indice_Uno]



def quick_sort (nombres: list, identidades: list, generos: list, poderes:list, alturas:list)-> list[int]:
    if len(poderes)<2:
        return poderes
    pivote = poderes.pop() 
    lista_poderes_mas_chicos = []
    lista_nom_mas_chicos = []
    lista_ident_mas_chicos = []
    lista_generos_mas_chicos = []
    lista_alturas_mas_chicos = []

    lista_poderes_mas_grandes = []
    lista_nom_mas_grandes = []
    lista_ident_mas_grandes = []
    lista_generos_mas_grandes = []
    lista_alturas_mas_grandes = []
    for numero in poderes:
        if numero <= pivote:
            lista_poderes_mas_chicos.append(numero)
            lista_nom_mas_chicos.append(nombres)
            lista_ident_mas_chicos.append(identidades)
            lista_generos_mas_chicos.append(generos)
            lista_alturas_mas_chicos.append(alturas)
        else:
            lista_poderes_mas_grandes.append(numero)
            lista_nom_mas_grandes.append(nombres)
            lista_ident_mas_grandes.append(identidades)
            lista_generos_mas_grandes.append(generos)
            lista_alturas_mas_grandes.append(alturas)

        return quick_sort(lista_poderes_mas_chicos) + [pivote] + quick_sort(lista_poderes_mas_grandes) 
