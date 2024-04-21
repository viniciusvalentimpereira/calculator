from art import logo
from operators import add, subtract, divide, multiply, potential

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "**": potential
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    persist = True

    while persist:
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to star a new calculation: ") == 'y':
            num1 = answer
        else:
            persist = False
            calculator()

calculator()