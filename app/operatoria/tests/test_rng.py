from doctest import DONT_ACCEPT_TRUE_FOR_1
from random import randint, seed
from unittest import TestCase
from app.shared.core import pass_test_for_now
from operatoria.classes import Resta, Suma
from shared.enums import Dificulty
from operatoria.classes import Question

'''
Tests de Question
'''
class RandomNumberGeneratorClass(TestCase):
    def setUp(self) -> None:
        seed(0)
        
    def test_get_random_factors_by_dificulty__EASY(self):
        question = Question(operation=Suma(), dificulty=Dificulty.EASY)
        random_numbers = [randint(0, 10), randint(0, 10)]
        self.assertListEqual(question.factors, random_numbers)
        
    def test_get_random_float_factors_by_dificulty(self):
        pass_test_for_now(self)
    
    def test_get_value_range_by_dificulty(self):
        pass_test_for_now(self)