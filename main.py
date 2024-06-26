from art import logo

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide }




def first(num1, op_symbol, num2):
    action = operations[op_symbol]
    previous_answer = action(num1, num2)
    return(previous_answer)
    

def cont_calculating(previous, op_symbol, num3):
    action = operations[op_symbol]
    sec_answer = action(previous, num3)
    return(sec_answer)

def main():
    print(logo)
    calculating = True
    previous_answer = 0
    sec_answer = 0
    num1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)
    op_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    previous_answer = first(num1, op_symbol, num2)
    print(f"{num1} {op_symbol} {num2} = {previous_answer}")

    while calculating:
        ask = input(f"Type 'y' to continue calculating with {previous_answer}, type 'x' to start a new calculation, or type 'n' to exit.: ").lower()
        if ask == "n":
            calculating = False
        elif ask == 'x':
            calculating = False
            main()
        else:
            op_symbol = input("Pick an operation: ")
            num3 = float(input("What's the next number?: "))
            sec_answer = cont_calculating(previous_answer, op_symbol, num3)
            print(f"{previous_answer} {op_symbol} {num3} = {sec_answer}")
            previous_answer = sec_answer


main()