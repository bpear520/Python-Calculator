def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def exp(a, b):
    return a ** b

def mod(a, b):
    return a % b

operations {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "^": exp,
    "%": mod,
}

num1 = input("Whats the first number?: ")
num2 = input("Whats the second number?: ")

for functions in operations:
    print(operations[functions])