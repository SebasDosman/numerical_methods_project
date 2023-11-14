import math

import numpy as np

from numerical_methods.calculate_equation_systems.helpers import TOLERANCE


def calculate_error(x1 : float, x0 : float, y1 : float, y0 : float, z1 : float, z0 : float, pow : float) -> float:
    sum_1 = (math.pow(x1 - x0, pow) + math.pow(y1 - y0, pow) + math.pow(z1 - z0, pow))
    sum_2 = (math.pow(x1, pow) + math.pow(y1, pow) + math.pow(z1, pow))
    
    return (math.pow(sum_1, 1 / pow) / math.pow(sum_2, 1 / pow))

def jacobi(f1 : callable, f2 : callable, f3 : callable, pow : float, iterations : int, tol = TOLERANCE) -> None:
    x0 = 0; y0 = 0; z0 = 0
    
    for i in range(iterations):
        x1 = f1(x0, y0, z0)
        y1 = f2(x0, y0, z0)
        z1 = f3(x0, y0, z0)
        
        error = calculate_error(x1, x0, y1, y0, z1, z0, pow)
        
        if error <= tol:
            break
        else:
            x0 = x1
            y0 = y1
            z0 = z1
        
        print('x: {:<10}\ny: {:<10}\n z: {:<10}\nError: {:<10}'.format(x1, y1, z1, error))

def display_jacobi(pow : float, iterations : int) -> None:
    f1 = lambda x, y, z : ((4 - y - 2 * z) / 3)
    f2 = lambda x, y, z : ((6 - 2 * x - z) / 1)
    f3 = lambda x, y, z : ((2 - x - 4 * y) / 6)
    
    jacobi(f1, f2, f3, pow, iterations)