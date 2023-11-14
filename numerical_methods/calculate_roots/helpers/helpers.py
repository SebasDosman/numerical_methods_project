TOLERANCE = 0.000001

def calculate_error(current : float, previous : float) -> float:
    return abs((current - previous) / current)