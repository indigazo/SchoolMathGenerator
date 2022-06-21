"""
Core es donde se guardan las CLASES principales
aqui deberia ir las preguntas, prueba y todos sus metodos
logica de API se verda en otro lado, despues
"""
from dataclasses import dataclass
from functools import reduce
from typing import List
from shared.enums import Dificulty
from shared.enums import Dificulty as en_dif, EnumOperation as en_op
from abc import ABC, abstractmethod

#@TODO: Implementar get_random_factors, cambiar a que sea un metodo
# de operation en caso de no ingresar factores
class Operation(ABC):
    """Abstract class para crear operaciones matematicas"""
    @abstractmethod
    def get_operation_symbol(self) -> str:
        """Retorna el simbolo(s) que utiliza esta operacion"""
    
    @abstractmethod
    def get_result(self, factors: List[int]) -> int:
        """Retorna el resultado de la operacion: sobreescribir"""
    

class Suma(Operation):
    """Clase para crear una operacion suma"""
    def get_operation_symbol(self) -> str:
        return "+"
    
    def get_result(self, factors: List[int]) -> int:
        return reduce(lambda x, y : x + y, factors)


class Resta(Operation):
    """Clase para crear una operacion resta"""
    def get_operation_symbol(self) -> str:
        return "-"

    def get_result(self, factors: List[int]) -> int:
        return factors[0] - sum(factors[1:])

#@TODO: Setup random number generator class?
# https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
"""
Recibe el tipo de Operation, numero de factores y opcionalmente la dificultad :
Debe generar N factores que se le pidan adaptandose a los parametros de la clase
Operation, por lo que sera necesario implementar la info necesaria para factores
desde Operation. 
"""
class RandomFactorGenerator():
    
    def __init__(self, operation: Operation, n_factors: int, dificulty: Dificulty = Dificulty.EASY) -> None:
        self.operation = operation
        self.n_factors = n_factors
        self.dificulty = dificulty

    def get_random_factors(self):
        pass

    def get_random_factors_by_dificulty(self):
        pass


class Question():
    """
    Clase que representa una pregunta
    operation : Operation = clase heredada de operacion de la que obtendremos resultado
    factors : int[] = factores que se usaran para calcular la operatoria
    """
    def __init__(self, operation: Operation, dificulty: Dificulty = Dificulty.INTERMEDIATE, factors: List[int] = []) -> None:
        self.operation = operation
        self.dificulty = dificulty
        self.factors = factors
        
        # Si no recibe factores, retorna 2 factores basandose en la dificultad entregada (INT by default)
        if len(self.factors) == 0:
            rand = RandomFactorGenerator(self.operation, 2, self.dificulty)
            self.factors = rand.get_random_factors()


    def __str__(self) -> str:
        """Cambiada para que print(question) retorne el ejercicio y su respuesta """
        return f"{self.get_question_string()} = {self.operation.get_result(self.factors)}"

    
    def get_question_string(self) -> str:
        """ Deberia retornar {factor} {simbolo} {factor} """
        factors_str = [str(factor) for factor in self.factors]
        symbol_final = f" {self.operation.get_operation_symbol()} "
        return symbol_final.join(factors_str)




