def add(a, b):
    print(f'{a} + {b} = {a + b}')
def subtract(a, b):
    print(f'{a} - {b} = {a - b}')
def multiply(a, b):
    print(f'{a} * {b} = {a * b}')
def divide(a, b):
    print(f'{a} / {b} = {a / b}')

def getData(msg, check):
    data = input(msg)
    if check == 'operation':
        if data.isnumeric():
            data = int(data)
            if data > 0 and data <= 4:
                return data
    elif check == 'float':
        try:
            data = float(data)
            return data
        except ValueError:
            pass
    elif check == 'float_positive':
        try:
            data = float(data)
            if (data > 0):
                return data
        except ValueError:
            pass
    elif check == 'yes/no':
        if data == 'yes' or data == 'no':
            return data
    print("\nInvalid value. Let's try again!")
    return getData(msg, check)

def start():
    text = """Select operation.
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    Enter choice: (1/2/3/4):"""
    operation = getData(text, 'operation')
    a = getData('Enter first number:', 'float')
    b = getData('Enter second number:', 'float_positive' if operation == 4 else 'float')
    if operation == 1:
        add(a, b)
    elif operation == 2:
        subtract(a, b)
    elif operation == 3:
        multiply(a, b)
    elif operation == 4:
        divide(a, b)
    question = 'Would you like to do a new calculation? (yes/no):'
    if getData(question, 'yes/no') == 'yes':
        start()

start()