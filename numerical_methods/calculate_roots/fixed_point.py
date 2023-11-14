from numerical_methods.calculate_roots.helpers import TOLERANCE, calculate_error


def fixed_point(x : float, f : callable, tol = TOLERANCE) -> None:
    previous = x
    error = 0
    
    for i in range(50):
        current = f(previous)
        error = calculate_error(current, previous)
        
        if error<= tol:
            print('Raíz: {:<10}\nError: {:<10}'.format(current, error))
            
            return
        else:
            previous = current
    
    print('No se encontró una raíz')