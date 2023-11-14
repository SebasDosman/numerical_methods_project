import numpy as np


def simpson_rule_one_eight(a : float, b : float, function : callable) -> None:
    xi = np.linspace(a, b, 3)
    
    area = ((b - a) * ((function(xi[0]) + (4 * function(xi[1])) + function(xi[2])) / 6))
    
    print('Área: {:<10}'.format(area))

def simpson_rule_one_eight_composite(a : float, b : float, n : float, function : callable) -> None:
    area = 0
    
    if not n % 2 == 0:
        n = (2 * n)
    
    xi = np.linspace(a, b, n + 1)
    
    for i in range(1, n):
        if i % 2 == 0:
            area += 2 * function(xi[i])
        else:
            area += 4 * function(xi[i])
    
    area = ((b - a) * ((function(xi[0]) + area + function(xi[n])) / (3 * n)))
    
    print('Área: {:<10}'.format(area))

def simpson_rule_three_eight(a : float, b : float, function : callable) -> None:
    xi = np.linspace(a, b, 4)
    
    area = ((b - a) * (function(xi[0]) + (3 * function(xi[1]) + (3 * function(xi[2])) + function(xi[3])) / 8))
    
    print('Área: {:<10}'.format(area))

def simpson_rule_three_eight_composite(a : float, b : float, n : float, function : callable) -> None:
    area = 0
    
    if not n % 3 == 0:
        n = (3 * n)
    
    xi = np.linspace(a, b, n + 1)
    
    for i in range(n // 3):
        area += 3 * function(xi[(3 * i) + 1])
    
    for i in range(n // 3):
        area += 3 * function(xi[(3 * i) + 2])
    
    for i in range((n // 3) - 1):
        area += 2 * function(xi[(3 * i) + 3])
    
    area = ((3 * (b - a)) * ((function(xi[0]) + area + function(xi[n])) / (8 * n)))
    
    print('Área: {:<10}'.format(area))