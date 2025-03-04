# Loan calc

"""This module is a loan calculator, it should return the monthly payment"""
def prompt(message):
    """Print a formatted message"""
    print(f'==> {message}')

def invalid_number(number_str):
    """Rules out invalid numbers"""
    try:
        float(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Monthly Payment Calculator... Lets get started!')

while True:
    prompt('What is your loan amount?')
    principle = input()

    while invalid_number(principle):
        prompt('Please enter a positive number with no dollar sign.')
        principle = input()
    while float(principle) < 1:
        prompt('Number must be 1 or greater.')
        principle = input()

    prompt('What is your APR?')
    user_input = input()

    while invalid_number(user_input):
        prompt('Please enter a positive number with no percentage sign.')
        user_input = input()

    if float(user_input) < 1:
        month_interest = float(user_input) / 12
    else:
        month_interest = (float(user_input) / 12) / 100

    prompt('How many months will you need to pay back your loan?')
    duration = input()
    while float(duration) < 2:
        prompt('Number must be 2 or greater.')
        duration = input()

    while invalid_number(duration):
        prompt('Please enter a positive number of months.')
        duration = float(input())

    if month_interest != 0:
        monthly_payment = float(principle) * (
            month_interest / (1 - ((1 + month_interest) ** -float(duration))))
    else:
        monthly_payment = principle / duration

    prompt(f'Your payment will be ${monthly_payment:.2f} for {duration} months.')
    while True:
        prompt('Would you like to try again? (y/n)')
        answer = input().lower()
        if answer in ['y', 'n']:
            break
    if answer != 'y':
        break
prompt('Thank you for using the Monthly Payment Calculator!')
