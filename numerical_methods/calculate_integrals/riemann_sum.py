import numpy as np

from numerical_methods.calculate_integrals.helpers import calculate_dx


def riemann_sum_left(a : float, b : float, n : float, function : callable) -> None:
    dx = calculate_dx(a, b, n)
    xi = np.linspace(a, b, n + 1)
    a = 0
    
    for i in range(0, n):
        a += dx * function(xi[i])
    
    print('Área: {:<10}'.format(a))

def riemann_sum_middle(a : float, b : float, n : float, function : callable) -> None:
    dx = calculate_dx(a, b, n)
    xi = np.linspace(a, b, n + 1)
    a = 0
    
    for i in range(1, n + 1):
        mk = ((xi[i] + xi[i - 1]) / 2)
        a += dx * function(mk)
    
    print('Área: {:<10}'.format(a))

def riemann_sum_right(a : float, b : float, n : float, function : callable) -> None:
    dx = calculate_dx(a, b, n)
    xi = np.linspace(a, b, n + 1)
    a = 0
    
    for i in range(1, n + 1):
        a += dx * function(xi[i])
    
    print('Área: {:<10}'.format(a))

def riemann_sum_trapezoidal(a : float, b : float, n : float, function : callable) -> None:
    dx = calculate_dx(a, b, n)
    xi = np.linspace(a, b, n + 1)
    a = 0
    
    for i in range(0, n):
        a += dx * ((function(xi[i]) + function(xi[i + 1])) / 2)
    
    print('Área: {:<10}'.format(a))

def riemann_sum_trapezoidal_full(a : float, b : float, n : float, function : callable) -> None:
    xi = np.linspace(a, b, n + 1)
    area = 0
    
    for i in range(1, n):
        area += (function(xi[i]))
    
    result = ((b - a) * ((function(xi[0]) + (2 * area) + function(xi[n])) / (2 * n)))
    
    print('Área: {:<10}'.format(result))