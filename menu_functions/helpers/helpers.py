import os

import matplotlib.pyplot as plt
import numpy as np

from math_functions import cos_function


def display_main_menu() -> None:
    from menu_functions import main_menu
    main_menu()

def clear_screen() -> None:
    os.system('clear' if os.name == 'posix' else 'cls')

def calculate_gx(f : callable, x : float) -> callable:
    return lambda x: x - f(x)

def graphic_function(f : callable, x_range = (-200, 200), step = 0.1) -> None:
    x = np.arange(x_range[0], x_range[1], step)
    y = []
    
    for val in x:
        try:
            y_val = f(val)
            y.append(y_val)
        except:
            y.append(float('nan'))
    
    plt.figure(figsize = (8,6))
    plt.plot(x, y, label = str(f.__name__))
    
    plt.axhline(0, color='black',linewidth=1) 
    plt.axvline(0, color='black',linewidth=1)
    
    plt.title('Gráfico de {}'.format(f.__name__))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def create_intervals_matrix(n_intervals : int, period = (np.pi / 7.5)) -> list:
    initial_intervals = []
    superior_limit = period
    inferior_limit = 0
    
    for i in range(0, n_intervals):
        initial_intervals.append([inferior_limit, superior_limit])
        inferior_limit, superior_limit = superior_limit, (superior_limit + period)
    
    return np.array(initial_intervals)

def find_intervals_with_root(f : callable, intervals_evaluate : list) -> list:
    condition = (f(intervals_evaluate[:,0]) * f(intervals_evaluate[:,1])) < 0
    
    sublist_with_roots = intervals_evaluate[condition] 
    
    return np.array(sublist_with_roots)

def find_roots(method : callable, n_intervals : int) -> None:
    intervals_with_root = find_intervals_with_root(cos_function, create_intervals_matrix(n_intervals))
    
    for sublist in intervals_with_root:
        method(sublist[0], sublist[1], cos_function)