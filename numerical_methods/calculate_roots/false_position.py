from numerical_methods.calculate_roots.helpers import TOLERANCE, calculate_error


def false_position(a : float, b : float, f : callable, tol = TOLERANCE) -> None:
    previous = a
    error = 0
    
    for i in range(50):
        if (f(a) * f(b)) < 0:
            current = (a - (((a - b) * f(a)) / (f(a) - f(b))))
        
        error = calculate_error(current, previous)
        
        if error <= tol:
            print('Raíz: {:<10}\nError: {:<10}'.format(current, error))
            
            return
        
        if (f(a) * f(current)) < 0:
            b = current
            previous = b
        else:
            a = current
            previous = a
    
    print('No se encontró una raíz')