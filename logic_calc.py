def add(a, b):
    return a + b

def subtruct(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Делить на ноль нельзя"