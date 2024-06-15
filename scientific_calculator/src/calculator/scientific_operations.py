import math

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def log(x):
    if x <= 0:
        raise ValueError("Math domain error")
    return math.log(x)
