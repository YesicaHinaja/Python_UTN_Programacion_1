from funciones import mostrar_menu, play_sound, limpiar_pantalla #IMPORTAMOS FUNCIONES DE OTROS PAQUETES
from validaciones import  validar_opcion
from funciones.funciones_utn import utn_mostrar_mayor_altura, utn_mostrar_identidades_heroes, utn_mostrar_nombres_heroes, utn_mostrar_heroes_mas_fuertes,\
    utn_mostrar_heroes_poder_superior_promedio, utn_filtrar_heroes_genero, utn_mostrar_heroes_mas_debiles,  utn_mostrar_heroes_poder_ascendente

def utn_heroes_app (lista_nombres: list, lista_generos: list, lista_identidades: list, lista_poderes: list, lista_alturas: list):

    while True:
        mostrar_menu()
        opcion = validar_opcion(1,10)
        play_sound()
        
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
                
            case 2: 
                utn_mostrar_identidades_heroes(lista_identidades)
                
            case 3: 
                utn_mostrar_mayor_altura(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
                
            case 4: 
                utn_mostrar_heroes_mas_fuertes(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
                
            case 5: 
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades,lista_generos, lista_poderes, lista_alturas, 'Femenino')
                
            case 6: 
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades,lista_generos, lista_poderes, lista_alturas, 'Masculino')
                
            case 7:  #NO MUESTRA POR CONSOLA: ARREGLAR
                utn_filtrar_heroes_genero(lista_nombres, lista_identidades,lista_generos, lista_poderes, lista_alturas, 'No-binario')
                
            case 8: 
                utn_mostrar_heroes_poder_superior_promedio(lista_nombres, lista_identidades, lista_generos, lista_poderes, lista_alturas)
                
            case 9: 
                utn_mostrar_heroes_mas_debiles(lista_nombres, lista_identidades,lista_generos, lista_poderes, lista_alturas)
                
            case 10: 
                utn_mostrar_heroes_poder_ascendente (lista_poderes, lista_nombres)
            case 11:
                pass
            case 12: 
                pass
            case 13:
                break
        limpiar_pantalla()
