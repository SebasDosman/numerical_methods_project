from derivative_methods import derivate
from numerical_methods.calculate_roots.helpers import TOLERANCE, calculate_error


def newton_raphson(x : float, f : callable, tol = TOLERANCE) -> None:
    previous = x
    error = 0
    
    for i in range(50):
        current = previous - (f(previous) / derivate(previous, f))
        error = calculate_error(current, previous)
        
        if error <= tol:
            print('Raíz: {:<10}\nError: {:<10}'.format(current, error))
            
            return
        else:
            previous = current
    
    print('No se encontró una raíz')