from derivative_methods import derivate
from numerical_methods.calculate_roots.helpers import TOLERANCE, calculate_error


def secant(a: float, b : float, f : callable, tol = TOLERANCE) -> None:
    for i in range(50):
        derivative = derivate(a, f)
        position = a - (f(a) / derivative)
        error = calculate_error(position, a)
        
        if error <= tol:
            print('Raíz: {:<10}\nError: {:<10}'.format(a, error))
            
            return
        
        a = b
        b = position
    
    print('No se encontró una raíz')