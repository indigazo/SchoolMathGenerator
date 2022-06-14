from unittest import TestCase
from operatoria.classes import RestaEnteros, SumaEnteros
from shared.enums import EnumDificulty
from operatoria.classes import Question

'''
Tests de Question
'''
class TestClassQuestion(TestCase):
    def setUp(self) -> None:
        """Seteamos la suma operacion random que usaremos para probar el concepto"""
        self.suma = SumaEnteros()
    
    def test_create_with_factors(self):
        pass
        
    def test_no_factors(self):
        """Probamos que a pesar de entrar sin factores, le genero 2"""
        question = Question(operation=self.suma, dificulty=EnumDificulty.EASY, factors=[])
        self.assertEqual(len(question.factors), 2)
    