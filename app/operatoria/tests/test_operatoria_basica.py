from unittest import TestCase
from operatoria.classes import Resta, Suma
from shared.enums import Dificulty
from operatoria.classes import Question

'''
Tests de Operatoria: Suma
'''
class Operatoria__Suma(TestCase):
    def setUp(self) -> None:
        self.question = Question(operation=Suma(), dificulty=Dificulty.EASY, factors=[1, 1])

    def test_get_operation_symbol(self):
        self.assertEqual(self.question.operation.get_operation_symbol(), "+")

    def test_get_result(self):
        self.assertEqual(self.question.operation.get_result(self.question.factors), 2)

'''
Tests de Operatoria: Resta
'''
class Operatoria__Resta(TestCase):
    def setUp(self) -> None:
        self.question = Question(operation=Resta(), dificulty=Dificulty.EASY, factors=[1, 1])

    def test_get_operation_symbol(self):
        self.assertEqual(self.question.operation.get_operation_symbol(), "-")

    def test_get_result(self):
        self.assertEqual(self.question.operation.get_result(self.question.factors), 0)
