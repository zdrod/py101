# Account for bad input and divide by 0
def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... this doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... this doesn't look like a valid number.")
    number2 = input()

prompt('What Operation would you like to perform?\n'
      '1) Add\n2) Subtract\n3) Multiply\n4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4.')
    operation = input()

match operation:
    case '1': # '1' represents addition
        output = int(number1) + int(number2)
    case '2': # '2' represents subtraction
        output = int(number1) - int(number2)
    case '3': # '3' represents multiplication
        output = int(number1) * int(number2)
    case '4': # '4' represents division
        output = int(number1) / int(number2)
# We have not accounted for bad input or divide by 0

prompt(f'The result is: {output}')