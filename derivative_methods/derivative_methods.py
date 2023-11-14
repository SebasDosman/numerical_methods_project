import math


def derivate(x : float, f : callable, h = 0.001) -> float:
    return ((f(x + h) - f(x)) / h)

def second_derivate(x : float, f : callable, h = 0.001) -> float: 
    return ((f(x + 2 * h) - (2 * f(x + h)) + f(x))/ math.pow(h, 2))

def front_difference(x : float, h : float, f : callable) -> float:
    return ((f(x + h) - f(x)) / h)

def second_front_difference(x : float, h : float, f : callable) -> float:
    return ((f(x + (2 * h)) - (2 * f(x + h)) + f(x)) / math.pow(h, 2))

def back_difference(x : float, h : float, f : callable) -> float:
    return ((f(x) - f(x - h)) / h)

def second_back_difference(x : float, h : float, f : callable) -> float:
    return ((f(x) - (2 * f(x - h)) + f(x - (2 * h))) / math.pow(h, 2))

def center_difference(x : float, h : float, f : callable) -> float:
    return ((f(x + h) - f(x - h)) / (2 * h))

def second_center_difference(x : float, h : float, f : callable) -> float:
    return ((f(x + h) - (2 * f(x)) + f(x - h)) / math.pow(h, 2))