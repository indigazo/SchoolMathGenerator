'''
Funciones, Enums y clases de uso global: 
La idea de este file es poder convertirlo en un package
para futuros proyectos, ir agregando aqui todo lo necesario
'''
import glob
import os

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
    """ Elimina un grupo de archivos en un directorio dado un patron ej: /hom/user/*.txt """
    fileList = glob.glob(patron)

    # Recorre la lista y elimina los archivos
    for file in fileList:
        try:
            os.remove(file)
        except:
            print("Error al eliminar el archivo  : ", file)
     