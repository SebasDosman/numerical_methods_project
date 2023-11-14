def calculate_error(interpolation : float, f : callable, x : float):
    return abs((interpolation - f(x)) / f(x))