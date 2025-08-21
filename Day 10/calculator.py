import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

session = True
cont = ""

print(art.logo)
def calculator(first, selected, second):
    result = operation[selected](first, second)
    return result

def to_continue(first, selected, second):
    result = operation[selected](first, second)
    return result

while session:
    num1 = float(input("What is the first number?: "))
    operator = input("Pick an operation: ")
    num2 = float(input("What is the second number: "))

    stored_number = calculator(num1, operator, num2)
    print(f"{num1} {operator} {num2} = {stored_number}")
    cont = input(f"Type 'y' to continue calculating with {stored_number}, or type 'n' to start a new calculation: ").lower()

    while cont == 'y':
        operator = input("Pick an operation")
        num2 = float(input("What is the second number: "))

        new_result = to_continue(stored_number, operator, num2)
        print(f"{stored_number} {operator} {num2} = {new_result}")
        stored_number = new_result
        cont = input(f"Type 'y' to continue calculating with {stored_number}, or type 'n' to start a new calculation: ").lower()
