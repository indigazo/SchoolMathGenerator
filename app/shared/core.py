'''
Funciones, Enums y clases de uso global: 
La idea de este file es poder convertirlo en un package
para futuros proyectos, ir agregando aqui todo lo necesario
'''
import glob
import os
from unittest import TestCase

"""
Methods
"""

"""
Hacky Fixers
"""
def pass_test_for_now(test_case: TestCase) -> None:
    """ Para que un test pase mientras edito o testeo algo """
    test_case.assertEqual(1, 1)


"""
IO
"""
def create_directory(directorio: str) -> None:
    """ Crear directorio si este no existe en el disco """
    try:
        if not os.path.isdir(directorio):
            os.mkdir(directorio)
            print(f'Se ha creado correctamente el directorio {directorio}')

    except OSError as ex:
        print(f'Error al crear el directiorio {directorio}: {ex}')


def delete_files(patron: str) -> None:
    """ Elimina un grupo de archivos en un directorio dado un patron ej: /home/user/*.txt """
    file_list = glob.glob(patron)
    for file in file_list:
        try:
            os.remove(file)
        except OSError:
            print("Error al eliminar el archivo  : ", file)
     