def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def division(n1,n2):
    if n2 == 0:
        raise ValueError("Cannot divide by 0")
    else:
        return n1 / n2

def multiply(n1,n2):
    return n1 * n2