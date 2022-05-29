def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate():

    print("""
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    """) 
    operation = input ("   Your Option:  ")
    

    num_1 = float(input('Please enter the first number: '))
    num_2 = float(input('Please enter the second number: '))

    if operation == '+':
        print("\n",num_1, "+", num_2, "=", add(num_1, num_2))

    elif operation == '-':
        print("\n",num_1, "-", num_2, "=", subtract(num_1, num_2))

    elif operation == '*':
        print("\n",num_1, "*", num_2, "=", multiply(num_1, num_2))

    elif operation == '/':
        print("\n",num_1, "/", num_2, "=", divide(num_1, num_2))

    else:
        print('You have not typed a valid operator, please run the program again.')
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print()
    else:
        again()

calculate()
