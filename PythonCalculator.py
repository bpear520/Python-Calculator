from CalculatorLogo import logo
import os


# Various Calculator functions
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


# library for usable functions
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
    "^": exp,
    "%": mod,
}


# calculator interface uses recursion until getting to return statement
# calculator clears screen if the user decides to do a new calculation.
def calculator():
    os.system('cls')
    print(logo)

    num1 = float(input("Whats the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_calculating = True

    while continue_calculating:
        operation_symbol = input("Please pick an operation to do: ")
        num2 = float(input("Whats the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_choice = input(f"Type 'y' to continue calculating with {answer},"
                            f" type 'n' to start a new calculation, or type 'e' to exit program: ")
        if user_choice == 'y':
            num1 = answer
        elif user_choice == 'n':
            continue_calculating = False
            calculator()
        else:
            done = True
            return done


# while loop waits for done_calculating flag to be true so it can exit program
done_calculating = False
while done_calculating is not True:
    done_calculating = calculator()
