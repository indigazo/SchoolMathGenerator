from unittest import TestCase
from shared.core import get_random_factors
from operatoria.classes import RestaEnteros, SumaEnteros
from shared.enums import EnumDificulty
from operatoria.classes import Question

'''
Tests de Operatoria: Suma
'''
class TestClassesOperatoria_SumaEnteros(TestCase):
    def setUp(self) -> None:
        self.suma = SumaEnteros(factors=[1,1])
        self.question = Question(operation=self.suma, dificulty=EnumDificulty.EASY)

    def test_get_operation_symbol(self):
        self.assertEqual(self.suma.operation_symbol, "+")

    def test_get_result(self):
        self.assertEqual(self.suma.get_result(), 2)


class TestsQuestion_SumaEnteros(TestCase):
    def setUp(self) -> None:
        self.suma = SumaEnteros(factors=[1, 1])
        self.question = Question(operation = self.suma, dificulty=EnumDificulty.EASY)

    def test_render_question(self):
        self.assertEqual(self.question.get_question_string(), "1 + 1")

    def test_str_method(self):
        self.assertEqual(self.question.__str__(), "1 + 1 = 2")




'''
Tests de Operatoria: Resta
'''
class TestClassesOperatoria_RestaEnteros(TestCase):
    def setUp(self) -> None:
        self.resta = RestaEnteros(factors=[1, 1])
        self.question = Question(operation=self.resta, dificulty=EnumDificulty.EASY)

    def test_get_operation_symbol(self):
        self.assertEqual(self.resta.operation_symbol, "-")

    def test_get_result(self):
        self.assertEqual(self.resta.get_result(), 0)


class TestsQuestion_RestaEnteros(TestCase):
    def setUp(self) -> None:
        resta = RestaEnteros(factors=[1, 1])
        self.question = Question(operation = resta, dificulty=EnumDificulty.EASY)

    def test_render_question(self):
        self.assertEqual(self.question.get_question_string(), "1 - 1")

    def test_str_method(self):
        self.assertEqual(self.question.__str__(), "1 - 1 = 0")
