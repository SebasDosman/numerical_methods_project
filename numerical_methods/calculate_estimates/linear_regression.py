import math
import numpy as np


def linear_regression_simple(x_data : list, y_data : list) -> tuple:
    sum_xy = 0; sum_x = 0; sum_y = 0; sum_x2 = 0
    n = len(x_data)
    
    for i in range(n):
        sum_xy += x_data[i] * y_data[i]
        sum_x += x_data[i] 
        sum_y += y_data[i]
        sum_x2 += math.pow(x_data[i], 2)
    
    a1 = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x2) - math.pow(sum_x, 2))
    
    y_media = (sum_y / len(y_data))
    x_media = (sum_x / len(x_data))
    a0 = (y_media - (a1 * x_media))
    
    print('a0: {:<10}\na1: {:<10}'.format(a0, a1))

def display_linear_regression_simple() -> None:
    x_data = np.array([1.1, 2, 3.01, 4, 4.98, 6, 7.02, 8])
    y_data = np.array([2.5, 5.1, 8, 9.6, 10.8, 14, 15.1, 18])
    
    linear_regression_simple(x_data, y_data)

def linear_regression_multiple(x_data : list, y_data : list) -> tuple:
    sum_x = 0; sum_x2 = 0; sum_x3 = 0; sum_x4 = 0; sum_x2y = 0; sum_y = 0; sum_xy = 0
    n = len(x_data)
    
    for i in range(n):
        sum_x += x_data[i] 
        sum_x2 += math.pow(x_data[i], 2)
        sum_x3 += math.pow(x_data[i], 3)
        sum_x4 += math.pow(x_data[i], 4)
        sum_y += y_data[i]
        sum_xy += x_data[i] * y_data[i]
        sum_x2y += (math.pow(x_data[i], 2) * y_data[i])
    
    A = np.array([[n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    
    b = np.array([sum_y, sum_xy, sum_x2y])
    
    a0, a1, a2 = np.dot(np.linalg.inv(A), b)
    
    print('a0: {:<10}\na1: {:<10}\na2: {:<10}'.format(a0, a1, a2))

def display_linear_regression_multiple() -> None:
    x_data = np.array([1.1, 2.1, 3.01, 4, 4.98, 6.1, 7.02, 8, 9, 10])
    y_data = np.array([4.1, 5.2, 12.2, 19, 31, 43, 52, 71, 84.6, 104])
    
    linear_regression_multiple(x_data, y_data)