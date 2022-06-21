from unittest import TestCase
from operatoria.classes import Resta, Suma
from shared.enums import Dificulty
from operatoria.classes import Question

'''
Tests de Question
'''
class QuestionClass(TestCase):
    def setUp(self) -> None:
        """Seteamos la suma operacion random que usaremos para probar el concepto"""
        pass
    
    def test_create_with_factors(self):
        """Probamos que si la creo con N factores, se cree con esos N factores"""
        question = Question(operation=Suma(), dificulty=Dificulty.EASY, factors=[1, 1])
        self.assertEqual(len(question.factors), 2)
        
    def test_no_factors(self):
        """Probamos que a pesar de entrar sin factores, le genero 2"""
        question = Question(operation=Suma(), dificulty=Dificulty.EASY)
        self.assertEqual(len(question.factors), 2)

    def test_create_with_dificulty_INTERMEDIATE(self):
        """Chequear que los factores generados tengan 3 digitos maximo"""
        question = Question(operation=Suma(), dificulty=Dificulty.INTERMEDIATE)
        pass

    def test_create_with_dificulty_HARD(self):
        """Chequear que los factores generados tenga 4 o mas digitos"""
        question = Question(operation=Suma(), dificulty=Dificulty.HARD)
        pass

"""
Aqui pruebas de toda la operatoria usando la clase question
"""
class OperatoriaQuestionClass(TestCase):
    def setUp(self) -> None:
        self.question_suma = Question(operation=Suma(), dificulty=Dificulty.EASY, factors=[1, 1])
        self.question_resta = Question(operation=Resta(), dificulty=Dificulty.EASY, factors=[1, 1])

    def test_render_question__suma(self):
        self.assertEqual(self.question_suma.get_question_string(), "1 + 1")

    def test_str_method__suma(self):
        self.assertEqual(self.question_suma.__str__(), "1 + 1 = 2")