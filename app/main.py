"""
Para efectos de esta prueba esta funcion main deberia realizar lo siguiente :

recibir por parametro la dificultad, cantidad de preguntas y posibles
operaciones a utilizar en las preguntas.

Las preguntas estan contenidas en una clase llamada Prueba, que es solo un
conjunto de preguntas de X tipos (dificultades, operaciones, etc)

Retornar una "Prueba" en formato JSON y poder verlo en consola
"""
from operatoria.classes import Operation, Question
import shared.logger as logger 

LOG = logger.setup_custom_logger(__name__, 'main_math', 'logs_main_process')

    
def main() -> None:
    LOG.info("building main.py...")

if __name__ == "__main__":
    main()
