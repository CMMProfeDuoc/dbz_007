# juego de 'pelea'

from libreriaManejoArchivosDBZ import *

import herramientas

herramientas.limpiarPantalla()


mi_personaje = cargarPersonaje('1')

imprimirPersonaje(mi_personaje)

guardarPersonaje(mi_personaje)

"""
    Asignar un "usuario"

    Hacer menu con:
    - cargar personaje
    - guardar personaje
    - "cambiar" de personaje
    - "modificar" personaje
"""