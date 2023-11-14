import numpy as np

from numerical_methods.calculate_estimates.helpers import calculate_error


def newton_interpolation(a : float, b : float, n : int, f : callable, x : float) -> None:
    interval = np.linspace(a, b, n)
    matrix = np.zeros((n, n))
    
    for i in range(n):
        matrix[i, 0] = f(interval[i])
    
    for j in range(1, n):
        for i in range(n - j):
            matrix[i, j] = (matrix[i + 1, j - 1] - matrix[i, j - 1]) / (interval[i + j] - interval[i])
    
    result = matrix[0, 0]
    product_term = 1
    
    for i in range(1, n):
        product_term *= (x - interval[i - 1])
        result += matrix[0, i] * product_term
    
    sum, error = interpolation(matrix, n, interval, x, f)
    
    print('Sumatoria: {:<10}\nError: {:<10}'.format(sum, error))

def interpolation(matrix : list, n : int, interval : list, x : float, f : callable) -> tuple:
    list = []
    sum = f(interval[0])
    product_sum = 1
    
    for i in range(n):
        list.append(matrix[0, i])
    
    for i in range(1, n):
        sum += list[i] * product_sum
        product_sum *= x - interval[i]
    
    error = calculate_error(sum, f, x)
    
    return sum, error

def lagrange_interpolation(x_data : list, y_data : list, x : float) -> None:
    n = len(x_data)
    
    result = 0.0
    
    for i in range(n):
        term = y_data[i]
        
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        
        result += term
    
    print('Sumatoria: {:<10}'.format(result))

def display_lagrange_interpolation() -> None:
    x_data = [1.0, 2.0, 3.0, 4.0]
    y_data = [2.0, 1.0, 3.0, 5.0]
    x_interpolate = 2.5
    
    lagrange_interpolation(x_data, y_data, x_interpolate)