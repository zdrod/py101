import json

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def messages(message, lang=LANGUAGE):
    return MESSAGES[lang][message]

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    
    return False

prompt(messages('welcome'))
while True:
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(messages('invalid_number'))
        number1 = input()

    prompt("What's the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(messages('invalid_number'))
        number2 = input()

    prompt('What Operation would you like to perform?\n'
      '1) Add\n2) Subtract\n3) Multiply\n4) Divide')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('You must choose 1, 2, 3, or 4.')
        operation = input()

    match operation:
        case '1': # '1' represents addition
            output = float(number1) + float(number2)
        case '2': # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3': # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4': # '4' represents division
            output = float(number1) / float(number2)
    prompt(f'The result is: {output}')
    prompt('Would you like to go again? (y/n) ')
    answer = input()
    if answer and answer[0].lower() != 'y':
        break
# We have not accounted for bad input or divide by 0