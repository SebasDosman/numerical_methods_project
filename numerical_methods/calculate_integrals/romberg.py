import math

from numpy import zeros

from numerical_methods.calculate_integrals.helpers.helpers import TOLERANCE


def trapezoid(a : float, b : float, f : callable, Iold : float, k : int) -> float:
    if k == 1 : Inew = ((f(a) + f(b)) * (b - a) / 2.0)
    
    else:
        n = (2 ** (k - 2))     
        h = ((b - a) / n)      
        x = ((a + h) / 2.0)
        
        sum = 0.0
        
        for i in range(n):
            sum = sum + f(x)
            x = x + h
        
        Inew = ((Iold + (h * sum)) / 2.0)
    
    return Inew

def romberg(a : float, b : float, f : callable, tol = TOLERANCE) -> None:
    def richardson(r, k):
        for j in range(k - 1, 0, -1):
            const = (4.0 ** (k - j))
            r[j] = ((const * r[j + 1] - r[j]) / (const - 1.0))
        
        print('Área: {}'.format(r))
    
    r = zeros(21)
    r[1] = trapezoid(a, b, f, 0.0, 1)
    r_old = r[1]
    
    for k in range(2, 21):
        r[k] = trapezoid(a, b, f, r[k - 1], k)
        r = richardson(r, k)
        
        if abs(r[1] - r_old) < tol * max(abs(r[1]), 1.0):
            print(r[1])
        
        r_old = r[1]
    
    print('Romberg no converge')