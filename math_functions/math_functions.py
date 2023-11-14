import math

import numpy as np


def euler_function(x : float) -> float:
    return (math.exp(-x) - x);

def log_function(x : float) -> float:
    return (math.log(x));

def cos_function(x : float) -> float:
    return np.cos(x)

def x_function(x : float) -> float:
    return (math.pow(x, 2) - 8);

def x2_function(x : float) -> float:
    return math.sqrt(x + 1)

def t_function(t : float) -> float:
    return ((20 * math.exp(0.15 * t)) - 100);

def select_function() -> dict:
    functions  = {
        '1': ('e^x - x', euler_function),
        '2': ('Ln(x)', log_function),
        '3': ('Cos(x)', cos_function),
        '4': ('x^2 - 8', x_function),        
        '5': ('x^(1/2) + 1', x2_function),
        '6': ('20^(0.15*t) - 100', t_function)
    }
    
    print('¿Qué función desea utilizar?\n')
    
    for key, value in functions.items():
        print('{}. {}'.format(key, value.__getitem__(0)))	
    
    choice = input('\nSeleccione una opción: ')
    
    while choice not in functions:
        print('\n¡Opción inválida! Por favor ingrese otra opción')
        choice = input('\nSeleccione una opción: ')
    
    return functions[choice][1]