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

#FUNCIONES A DESARROLLAR 
from .funciones_utn import (
    utn_filtrar_heroes_genero, utn_mostrar_mayor_altura,
    utn_mostrar_heroes_mas_fuertes, utn_mostrar_identidades_heroes,
    utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_mas_debiles, utn_mostrar_heroes_poder_ascendente,utn_mostrar_heroes_asc_o_des,utn_mostrar_heroes_altura_descendente
)


#DEBEMOS IMPORTAR EN EL INIT LAS FUNCIONES DE LOS MODULOS DEL MISMO PAQUETE
#PARA QUE SEA MAS FACIL IMPORTAR LUEGO DESDE OTROS PAQUETES

from .auxiliares import play_sound, limpiar_pantalla, obtener_maximo, bubble_sort, selection_sort, quick_sort

#modulos y funciones creadas
from .salida_consola import mostrar_menu