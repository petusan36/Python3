"""
Programa de Prueba

Este es un Programa para realizar pruebas de ejecución

"""

import math

def num_to_exp(num, exp):
    """
    Esta función lo que hace es que eleva un numero segun un exponente
    Args:
    num (int): numero para exponer
    exp (int): exponente del numero

    Returns:
    Un numero (num) elevado a otro (exp)

    >>>num_to_exp(0,1)
    3
    """
    print (num ** exp)

num_to_exp(3,2)
