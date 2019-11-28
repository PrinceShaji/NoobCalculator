#!/usr/bin/env python3
# Noobie Calculator Generator.
#Inspired by https://github.com/AceLewis.


def generate_lines(operation, number_pool, output_file):
    """ This function generates and writes the new file. """
    for i in number_pool:
        line1 = f'if number1 == {i[0]} and operation == \'{operation}\' and number2 == {i[1]}:' + '\n'

        if operation == '+':
            line2 = f'\tprint("{i[0]}+{i[1]} = {i[0] + i[1]}")' + '\n'
        elif operation == '-':
            line2 = f'\tprint("{i[0]}-{i[1]} = {i[0] - i[1]}")' + '\n'
        elif operation == '*':
            line2 = f'\tprint("{i[0]}*{i[1]} = {i[0] * i[1]}")' + '\n'
        elif operation == '/':
            if i[1] == 0:
                line2 = f'\tprint("Cannot divide by Zero.")' + '\n'
            else:
                line2 = f'\tprint("{i[0]}/{i[1]} = {i[0] / i[1]}")' + '\n'
        else:
            print('Something went terribly wrong!')
            exit()
        
        output_file.write(line1)
        output_file.write(line2)
        


CALCULATOR_INTRO = r'''#!/usr/bin/env python3

# Welcome to my first calculator.
# Inspired by https://github.com/AceLewis.

# This calculator can calculate numbers from 1 to {}.

try:
    number1 = int(input('Enter first number: '))
    operation = input('Enter the operation [+, -, *, /]: ')
    number2 = int(input('Enter first number: '))
except:
    print('Only input digits.Try again.')

allowed_operations = ('+', '-', '*', '/')
print('\n')

if operation in allowed_operations:
    pass
else:
    print('Invalid operation!')
    exit()

'''

if __name__ == "__main__":
    # Filter out non decimal characters.
    try:
        MAX_RANGE = int(input('Enter the range of the calculator ( 1 to inf): '))
    except:
        print('Only input digits.Try again.')

    CALCULATOR_INTRO = CALCULATOR_INTRO.format(MAX_RANGE)
    OPERATIONS = ('+', '-', '*', '/')

    # Filter out negative numbers and zero.
    if MAX_RANGE >= 1:
        NUMBER_POOL = [(x, y) for x in range(MAX_RANGE + 1) for y in range(MAX_RANGE + 1)]
    else:
        print(f'{MAX_RANGE} is out of rage. Try again!')
        exit()

    with open(f'my_first_calculator_0_to_{MAX_RANGE}.py', 'w') as CALCULATOR:
        CALCULATOR.write(CALCULATOR_INTRO)
        for i in OPERATIONS:
            generate_lines(i, NUMBER_POOL, CALCULATOR)
        CALCULATOR.write('\nprint("\\nCheckout the original code by AceLewis on GitHub.\\nHave a good day!")')
