# Basic Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example Usage
result = add(5, 3)
print("Addition:", result)

result = subtract(8, 4)
print("Subtraction:", result)

result = multiply(2, 6)
print("Multiplication:", result)

result = divide(10, 2)
print("Division:", result)
