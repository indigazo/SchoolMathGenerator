'''
Funciones de uso global
Enums de uso global, etc.
'''

# Entrega un numero al azar, le tengo que dar un maximo 
import glob
import os
from shared.enums import EnumDificulty


def get_random_factor(max_size: int) -> int:
    pass


def get_random_factor_by_dificulty(dificultad: EnumDificulty) -> int:
    pass


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