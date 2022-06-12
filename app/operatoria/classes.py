"""
Core es donde se guardan las CLASES principales
aqui deberia ir las preguntas, prueba y todos sus metodos
logica de API se verda en otro lado, despues
"""
from dataclasses import dataclass
from typing import List, Tuple
from shared.enums import EnumDificulty
from shared.enums import EnumDificulty as en_dif, EnumOperation as en_op

#@TODO: Implementar get_random_factors, cambiar a que sea una funcion
# global en vez de que sea parte de operation

class Operation():
    '''
    Clase base para una operacion
    get_result()
    '''
    operation_symbol = ""

    def __init__(self, factors: List[int]) -> None:
        self.factors = factors

    # Posiblemente retornar una lista de factores?
    # def get_random_factors(self, dificulty: EnumDificulty, n_factors: int) -> List[int]:
    #     pass

    # Sobreescribir para describir como resolver esa operacion
    def get_result(self) -> int:
        pass


class SumaEnteros(Operation):
    '''
    Operacion suma N factores:
        A + B + N... = C
    '''
    operation_symbol = "+"

    def __init__(self, factors: List[int]) -> None:
        super().__init__(factors)

    # Para evitar escribir pruebas a mano, se puede obtener un ejercicio
    # random, usando la dificultad para obtener los factores de la operacion usada
    # def get_random_factors(self, dificulty: EnumDificulty, n_factors: int) -> List[int]:
    #     return super().get_random_factors(dificulty, n_factors)

    def get_result(self) -> int:
        result = 0
        for factor in self.factors:
            result += factor
        return result


class RestaEnteros(Operation):
    '''
    Operacion Resta N factores:
        A - B - N... = C
    '''
    operation_symbol = "-"

    def __init__(self, factors: List[int]) -> None:
        super().__init__(factors)

    def get_random_exercise(self) -> List[int]:
        pass

    def get_result(self) -> int:
        return self.factors[0] - sum(self.factors[1:])


class Question():
    '''
    Clase que representa una pregunta
    operation : Operation = clase heredada de operacion de la que obtendremos resultado
    factors : int[] = factores que se usaran para calcular la operatoria
    '''
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


