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
    def get_operation_symbol(self) -> str:
        """Retorna el simbolo(s) que utiliza esta operacion"""
        pass
    
    def get_result(self, factors) -> int:
        """Retorna el resultado de la operacion: sobreescribir"""
        pass


class SumaEnteros(Operation):
    def get_operation_symbol(self) -> str:
        return "+"
    
    def get_result(self, factors) -> int:
        return reduce(lambda x, y : x + y, factors)


class RestaEnteros(Operation):
    def get_operation_symbol(self) -> str:
        return "-"

    def get_result(self, factors) -> int:
        return factors[0] - sum(factors[1:])


class Question():
    """
    Clase que representa una pregunta
    operation : Operation = clase heredada de operacion de la que obtendremos resultado
    factors : int[] = factores que se usaran para calcular la operatoria
    """
    def __init__(self, operation: Operation, dificulty: EnumDificulty, factors: List[int] = []) -> None:
        self.operation = operation
        self.dificulty = dificulty
        self.factors = factors
        
        if len(self.factors) == 0:
            print("Genera factores random basandote en dificultad!")


    def __str__(self) -> str:
        """Cambiada para que print(question) retorne el ejercicio y su respuesta """
        return f"{self.get_question_string()} = {self.operation.get_result(self.factors)}"

    
    def get_question_string(self) -> str:
        """ Deberia retornar {factor} {simbolo} {factor} """
        factors_str = [str(factor) for factor in self.factors]
        symbol_final = f" {self.operation.get_operation_symbol()} "
        return symbol_final.join(factors_str)




