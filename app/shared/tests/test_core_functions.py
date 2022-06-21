import glob
import os
from unittest import TestCase

from app.shared.core import create_directory, delete_files

class OSFunctions(TestCase):
    """ Para probar las funciones genericas del core"""
    def setUp(self) -> None:
        self.test_dir = "app/media/test_folder"
        
        # Creacion de una carpeta con archivos falsos
        self.test_file_folder = "app/media/test_files/"
        self.patron_busqueda = self.test_file_folder + "*.txt"
        create_directory(self.test_file_folder)
        for i in range(50):
            with open(f"{self.test_file_folder}file_{i}.txt", 'w+') as text_file:
                text_file.write(f"This is test file number {i}")
    
    def test_create_directory(self):
        create_directory(self.test_dir)
        self.assertEqual(os.path.isdir(self.test_dir), True)
        
    def test_delete_files(self):
        delete_files(self.patron_busqueda)
        file_list = glob.glob(self.patron_busqueda)
        file_len = len(file_list)
        self.assertEqual(file_len, 0) 
        
    def tearDown(self) -> None:
        """ Limpia las carpetas/archivos creados por los tests"""
        if os.path.isdir(self.test_file_folder):
            delete_files(self.patron_busqueda)
            os.rmdir(self.test_file_folder)
        
        if os.path.isdir(self.test_dir):
            os.rmdir(self.test_dir)