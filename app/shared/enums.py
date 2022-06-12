'''
App wide Enums
'''
from enum import IntEnum, auto

# To identify the dificulty 
class EnumDificulty(IntEnum):
    EASY = auto()
    INTERMEDIATE = auto()
    HARD = auto()


# To identify the type of operation 
class EnumOperation(IntEnum):
    ADDITION = auto()
    SUBSTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
