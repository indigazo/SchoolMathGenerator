"""
Core es donde se guardan las CLASES principales
aqui deberia ir las preguntas, prueba y todos sus metodos
logica de API se verda en otro lado, despues
"""
from dataclasses import dataclass
from functools import reduce
from typing import List
from shared.enums import EnumDificulty
from shared.enums import EnumDificulty as en_dif, EnumOperation as en_op

#@TODO: Implementar get_random_factors, cambiar a que sea una funcion
# global en vez de que sea parte de operation

@dataclass
class Operation():
    """ Clase base para una operacion get_result()"""
    operation_symbol = ""
    factors: List[int]

    # Sobreescribir para describir como resolver esa operacion
    def get_result(self) -> int:
        pass


class SumaEnteros(Operation):
    operation_symbol = "+"
    
    def get_result(self) -> int:
        return reduce(lambda x, y : x + y, self.factors)


class RestaEnteros(Operation):
    operation_symbol = "-"

    def get_result(self) -> int:
        return self.factors[0] - sum(self.factors[1:])


class Question():
    """
    Clase que representa una pregunta
    operation : Operation = clase heredada de operacion de la que obtendremos resultado
    factors : int[] = factores que se usaran para calcular la operatoria
    """
    def __init__(self, operation: Operation, dificulty: EnumDificulty) -> None:
        self.operation = operation
        self.dificulty = dificulty

    # Cambiada para que print(question) retorne el ejercicio y su respuesta
    def __str__(self) -> str:
        return f"{self.get_question_string()} = {self.operation.get_result()}"

    # Deberia retornar {factor} {simbolo} {factor}
    def get_question_string(self) -> str:
        factors_str = [str(factor) for factor in self.operation.factors]
        symbol_final = f" {self.operation.operation_symbol} "
        return symbol_final.join(factors_str)


