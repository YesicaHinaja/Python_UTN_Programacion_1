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
    mixer.music.load('02_Desafios/Desafio_01/assets/snd/select.mp3')
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