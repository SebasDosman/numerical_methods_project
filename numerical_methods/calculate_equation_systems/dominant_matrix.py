import numpy as np

from numerical_methods.calculate_equation_systems.helpers import TOLERANCE


def dominant_matrix(A : list, b : list, pow : float, iterations : int, tol = TOLERANCE) -> None:
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    U = np.triu(A) - D
    
    T = -np.dot(np.linalg.inv(D), (L + U))
    c = np.dot(np.linalg.inv(D), b)
    
    x0 = np.array([0, 0, 0])
    
    for i in range(iterations):
        x1 = np.dot(T, x0,) + c
        error = (np.linalg.norm(x1 - x0, pow) / np.linalg.norm(x1, pow))
        
        if error <= tol:
            break
        else:
            x0 = x1
        
        print('x: {:<10}\ny: {:<10}\nz: {:<10}\nError: {:<10}'.format(x1[0], x1[1], x1[2], error))

def display_dominant_matrix(pow : float, iterations : int) -> None:
    A = np.array(
        [[3, 1, 2],
        [2, 1, 1],
        [1, 4, 6]]
    )
    
    b = np.array(
        [4, 6, 2]
    )
    
    dominant_matrix(A, b, pow, iterations)