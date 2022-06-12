'''
Funciones de uso global
Enums de uso global, etc.
'''

# Entrega un numero al azar, le tengo que dar un maximo 
import glob
import os
from typing import List
from shared.enums import EnumDificulty as en_dif


def get_random_factors(n_factors: int, dificulty: en_dif) -> List[int]:
    """ Obtiene N factores con en_dif dificultad """
    return [1, 1]   # joke 1 + 1 


def create_directory(directorio: str) -> None:
    """ Crear directorio si este no existe en el disco """
    try:
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
            print (f'Se ha creado correctamente el directorio {directorio}')

    except OSError:
        print (f'Error al crear el directiorio {directorio}')
        raise


def delete_files(patron: str) -> None:
    """ Elimina un grupo de archivos en un directorio dado un patron ejemplo /hom/user/rodrigo/*.txt """

    # genera la lista de archivos que cumplan con el patron
    fileList = glob.glob(patron)

    # Recorre la lista y elimina los archivos
    for file in fileList:
        try:
            os.remove(file)
        except:
            print("Error al eliminar el archivo  : ", file)
            raise