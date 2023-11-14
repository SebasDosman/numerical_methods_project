import math

from derivative_methods import derivate, second_front_difference
from numerical_methods.calculate_roots.helpers import TOLERANCE, calculate_error


def newton_raphson_multiple(a : float, f : callable, tol = TOLERANCE):
    for i in range(50):
        b = a - (f(a) * derivate(a, f) / ((math.pow(derivate(a, f), 2)) - (f(a) * second_front_difference(a, 0.0001 ,f))))
        error = calculate_error(b, a)
        
        if error <= tol:
            print('Raíz: {:<10}\nError: {:<10}'.format(a, error))
            
            return
        
        a = b
    
    print('No se encontró una raíz')