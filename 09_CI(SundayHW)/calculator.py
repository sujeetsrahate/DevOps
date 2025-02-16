def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
       raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Addition (3 + 5):", add(3, 5))
    print("Subtraction (10 - 4):", subtract(10, 4))
    print("Multiplication (6 * 7):", multiply(6, 7))
    print("Division (8 / 2):", divide(8, 2))
