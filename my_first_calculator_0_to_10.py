#!/usr/bin/env python3

# Welcome to my first calculator.
# Inspired by https://github.com/AceLewis.

# This calculator can calculate numbers from 1 to 10.

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

if number1 == 0 and operation == '+' and number2 == 0:
	print("0+0 = 0")
if number1 == 0 and operation == '+' and number2 == 1:
	print("0+1 = 1")
if number1 == 0 and operation == '+' and number2 == 2:
	print("0+2 = 2")
if number1 == 0 and operation == '+' and number2 == 3:
	print("0+3 = 3")
if number1 == 0 and operation == '+' and number2 == 4:
	print("0+4 = 4")
if number1 == 0 and operation == '+' and number2 == 5:
	print("0+5 = 5")
if number1 == 0 and operation == '+' and number2 == 6:
	print("0+6 = 6")
if number1 == 0 and operation == '+' and number2 == 7:
	print("0+7 = 7")
if number1 == 0 and operation == '+' and number2 == 8:
	print("0+8 = 8")
if number1 == 0 and operation == '+' and number2 == 9:
	print("0+9 = 9")
if number1 == 0 and operation == '+' and number2 == 10:
	print("0+10 = 10")
if number1 == 1 and operation == '+' and number2 == 0:
	print("1+0 = 1")
if number1 == 1 and operation == '+' and number2 == 1:
	print("1+1 = 2")
if number1 == 1 and operation == '+' and number2 == 2:
	print("1+2 = 3")
if number1 == 1 and operation == '+' and number2 == 3:
	print("1+3 = 4")
if number1 == 1 and operation == '+' and number2 == 4:
	print("1+4 = 5")
if number1 == 1 and operation == '+' and number2 == 5:
	print("1+5 = 6")
if number1 == 1 and operation == '+' and number2 == 6:
	print("1+6 = 7")
if number1 == 1 and operation == '+' and number2 == 7:
	print("1+7 = 8")
if number1 == 1 and operation == '+' and number2 == 8:
	print("1+8 = 9")
if number1 == 1 and operation == '+' and number2 == 9:
	print("1+9 = 10")
if number1 == 1 and operation == '+' and number2 == 10:
	print("1+10 = 11")
if number1 == 2 and operation == '+' and number2 == 0:
	print("2+0 = 2")
if number1 == 2 and operation == '+' and number2 == 1:
	print("2+1 = 3")
if number1 == 2 and operation == '+' and number2 == 2:
	print("2+2 = 4")
if number1 == 2 and operation == '+' and number2 == 3:
	print("2+3 = 5")
if number1 == 2 and operation == '+' and number2 == 4:
	print("2+4 = 6")
if number1 == 2 and operation == '+' and number2 == 5:
	print("2+5 = 7")
if number1 == 2 and operation == '+' and number2 == 6:
	print("2+6 = 8")
if number1 == 2 and operation == '+' and number2 == 7:
	print("2+7 = 9")
if number1 == 2 and operation == '+' and number2 == 8:
	print("2+8 = 10")
if number1 == 2 and operation == '+' and number2 == 9:
	print("2+9 = 11")
if number1 == 2 and operation == '+' and number2 == 10:
	print("2+10 = 12")
if number1 == 3 and operation == '+' and number2 == 0:
	print("3+0 = 3")
if number1 == 3 and operation == '+' and number2 == 1:
	print("3+1 = 4")
if number1 == 3 and operation == '+' and number2 == 2:
	print("3+2 = 5")
if number1 == 3 and operation == '+' and number2 == 3:
	print("3+3 = 6")
if number1 == 3 and operation == '+' and number2 == 4:
	print("3+4 = 7")
if number1 == 3 and operation == '+' and number2 == 5:
	print("3+5 = 8")
if number1 == 3 and operation == '+' and number2 == 6:
	print("3+6 = 9")
if number1 == 3 and operation == '+' and number2 == 7:
	print("3+7 = 10")
if number1 == 3 and operation == '+' and number2 == 8:
	print("3+8 = 11")
if number1 == 3 and operation == '+' and number2 == 9:
	print("3+9 = 12")
if number1 == 3 and operation == '+' and number2 == 10:
	print("3+10 = 13")
if number1 == 4 and operation == '+' and number2 == 0:
	print("4+0 = 4")
if number1 == 4 and operation == '+' and number2 == 1:
	print("4+1 = 5")
if number1 == 4 and operation == '+' and number2 == 2:
	print("4+2 = 6")
if number1 == 4 and operation == '+' and number2 == 3:
	print("4+3 = 7")
if number1 == 4 and operation == '+' and number2 == 4:
	print("4+4 = 8")
if number1 == 4 and operation == '+' and number2 == 5:
	print("4+5 = 9")
if number1 == 4 and operation == '+' and number2 == 6:
	print("4+6 = 10")
if number1 == 4 and operation == '+' and number2 == 7:
	print("4+7 = 11")
if number1 == 4 and operation == '+' and number2 == 8:
	print("4+8 = 12")
if number1 == 4 and operation == '+' and number2 == 9:
	print("4+9 = 13")
if number1 == 4 and operation == '+' and number2 == 10:
	print("4+10 = 14")
if number1 == 5 and operation == '+' and number2 == 0:
	print("5+0 = 5")
if number1 == 5 and operation == '+' and number2 == 1:
	print("5+1 = 6")
if number1 == 5 and operation == '+' and number2 == 2:
	print("5+2 = 7")
if number1 == 5 and operation == '+' and number2 == 3:
	print("5+3 = 8")
if number1 == 5 and operation == '+' and number2 == 4:
	print("5+4 = 9")
if number1 == 5 and operation == '+' and number2 == 5:
	print("5+5 = 10")
if number1 == 5 and operation == '+' and number2 == 6:
	print("5+6 = 11")
if number1 == 5 and operation == '+' and number2 == 7:
	print("5+7 = 12")
if number1 == 5 and operation == '+' and number2 == 8:
	print("5+8 = 13")
if number1 == 5 and operation == '+' and number2 == 9:
	print("5+9 = 14")
if number1 == 5 and operation == '+' and number2 == 10:
	print("5+10 = 15")
if number1 == 6 and operation == '+' and number2 == 0:
	print("6+0 = 6")
if number1 == 6 and operation == '+' and number2 == 1:
	print("6+1 = 7")
if number1 == 6 and operation == '+' and number2 == 2:
	print("6+2 = 8")
if number1 == 6 and operation == '+' and number2 == 3:
	print("6+3 = 9")
if number1 == 6 and operation == '+' and number2 == 4:
	print("6+4 = 10")
if number1 == 6 and operation == '+' and number2 == 5:
	print("6+5 = 11")
if number1 == 6 and operation == '+' and number2 == 6:
	print("6+6 = 12")
if number1 == 6 and operation == '+' and number2 == 7:
	print("6+7 = 13")
if number1 == 6 and operation == '+' and number2 == 8:
	print("6+8 = 14")
if number1 == 6 and operation == '+' and number2 == 9:
	print("6+9 = 15")
if number1 == 6 and operation == '+' and number2 == 10:
	print("6+10 = 16")
if number1 == 7 and operation == '+' and number2 == 0:
	print("7+0 = 7")
if number1 == 7 and operation == '+' and number2 == 1:
	print("7+1 = 8")
if number1 == 7 and operation == '+' and number2 == 2:
	print("7+2 = 9")
if number1 == 7 and operation == '+' and number2 == 3:
	print("7+3 = 10")
if number1 == 7 and operation == '+' and number2 == 4:
	print("7+4 = 11")
if number1 == 7 and operation == '+' and number2 == 5:
	print("7+5 = 12")
if number1 == 7 and operation == '+' and number2 == 6:
	print("7+6 = 13")
if number1 == 7 and operation == '+' and number2 == 7:
	print("7+7 = 14")
if number1 == 7 and operation == '+' and number2 == 8:
	print("7+8 = 15")
if number1 == 7 and operation == '+' and number2 == 9:
	print("7+9 = 16")
if number1 == 7 and operation == '+' and number2 == 10:
	print("7+10 = 17")
if number1 == 8 and operation == '+' and number2 == 0:
	print("8+0 = 8")
if number1 == 8 and operation == '+' and number2 == 1:
	print("8+1 = 9")
if number1 == 8 and operation == '+' and number2 == 2:
	print("8+2 = 10")
if number1 == 8 and operation == '+' and number2 == 3:
	print("8+3 = 11")
if number1 == 8 and operation == '+' and number2 == 4:
	print("8+4 = 12")
if number1 == 8 and operation == '+' and number2 == 5:
	print("8+5 = 13")
if number1 == 8 and operation == '+' and number2 == 6:
	print("8+6 = 14")
if number1 == 8 and operation == '+' and number2 == 7:
	print("8+7 = 15")
if number1 == 8 and operation == '+' and number2 == 8:
	print("8+8 = 16")
if number1 == 8 and operation == '+' and number2 == 9:
	print("8+9 = 17")
if number1 == 8 and operation == '+' and number2 == 10:
	print("8+10 = 18")
if number1 == 9 and operation == '+' and number2 == 0:
	print("9+0 = 9")
if number1 == 9 and operation == '+' and number2 == 1:
	print("9+1 = 10")
if number1 == 9 and operation == '+' and number2 == 2:
	print("9+2 = 11")
if number1 == 9 and operation == '+' and number2 == 3:
	print("9+3 = 12")
if number1 == 9 and operation == '+' and number2 == 4:
	print("9+4 = 13")
if number1 == 9 and operation == '+' and number2 == 5:
	print("9+5 = 14")
if number1 == 9 and operation == '+' and number2 == 6:
	print("9+6 = 15")
if number1 == 9 and operation == '+' and number2 == 7:
	print("9+7 = 16")
if number1 == 9 and operation == '+' and number2 == 8:
	print("9+8 = 17")
if number1 == 9 and operation == '+' and number2 == 9:
	print("9+9 = 18")
if number1 == 9 and operation == '+' and number2 == 10:
	print("9+10 = 19")
if number1 == 10 and operation == '+' and number2 == 0:
	print("10+0 = 10")
if number1 == 10 and operation == '+' and number2 == 1:
	print("10+1 = 11")
if number1 == 10 and operation == '+' and number2 == 2:
	print("10+2 = 12")
if number1 == 10 and operation == '+' and number2 == 3:
	print("10+3 = 13")
if number1 == 10 and operation == '+' and number2 == 4:
	print("10+4 = 14")
if number1 == 10 and operation == '+' and number2 == 5:
	print("10+5 = 15")
if number1 == 10 and operation == '+' and number2 == 6:
	print("10+6 = 16")
if number1 == 10 and operation == '+' and number2 == 7:
	print("10+7 = 17")
if number1 == 10 and operation == '+' and number2 == 8:
	print("10+8 = 18")
if number1 == 10 and operation == '+' and number2 == 9:
	print("10+9 = 19")
if number1 == 10 and operation == '+' and number2 == 10:
	print("10+10 = 20")
if number1 == 0 and operation == '-' and number2 == 0:
	print("0-0 = 0")
if number1 == 0 and operation == '-' and number2 == 1:
	print("0-1 = -1")
if number1 == 0 and operation == '-' and number2 == 2:
	print("0-2 = -2")
if number1 == 0 and operation == '-' and number2 == 3:
	print("0-3 = -3")
if number1 == 0 and operation == '-' and number2 == 4:
	print("0-4 = -4")
if number1 == 0 and operation == '-' and number2 == 5:
	print("0-5 = -5")
if number1 == 0 and operation == '-' and number2 == 6:
	print("0-6 = -6")
if number1 == 0 and operation == '-' and number2 == 7:
	print("0-7 = -7")
if number1 == 0 and operation == '-' and number2 == 8:
	print("0-8 = -8")
if number1 == 0 and operation == '-' and number2 == 9:
	print("0-9 = -9")
if number1 == 0 and operation == '-' and number2 == 10:
	print("0-10 = -10")
if number1 == 1 and operation == '-' and number2 == 0:
	print("1-0 = 1")
if number1 == 1 and operation == '-' and number2 == 1:
	print("1-1 = 0")
if number1 == 1 and operation == '-' and number2 == 2:
	print("1-2 = -1")
if number1 == 1 and operation == '-' and number2 == 3:
	print("1-3 = -2")
if number1 == 1 and operation == '-' and number2 == 4:
	print("1-4 = -3")
if number1 == 1 and operation == '-' and number2 == 5:
	print("1-5 = -4")
if number1 == 1 and operation == '-' and number2 == 6:
	print("1-6 = -5")
if number1 == 1 and operation == '-' and number2 == 7:
	print("1-7 = -6")
if number1 == 1 and operation == '-' and number2 == 8:
	print("1-8 = -7")
if number1 == 1 and operation == '-' and number2 == 9:
	print("1-9 = -8")
if number1 == 1 and operation == '-' and number2 == 10:
	print("1-10 = -9")
if number1 == 2 and operation == '-' and number2 == 0:
	print("2-0 = 2")
if number1 == 2 and operation == '-' and number2 == 1:
	print("2-1 = 1")
if number1 == 2 and operation == '-' and number2 == 2:
	print("2-2 = 0")
if number1 == 2 and operation == '-' and number2 == 3:
	print("2-3 = -1")
if number1 == 2 and operation == '-' and number2 == 4:
	print("2-4 = -2")
if number1 == 2 and operation == '-' and number2 == 5:
	print("2-5 = -3")
if number1 == 2 and operation == '-' and number2 == 6:
	print("2-6 = -4")
if number1 == 2 and operation == '-' and number2 == 7:
	print("2-7 = -5")
if number1 == 2 and operation == '-' and number2 == 8:
	print("2-8 = -6")
if number1 == 2 and operation == '-' and number2 == 9:
	print("2-9 = -7")
if number1 == 2 and operation == '-' and number2 == 10:
	print("2-10 = -8")
if number1 == 3 and operation == '-' and number2 == 0:
	print("3-0 = 3")
if number1 == 3 and operation == '-' and number2 == 1:
	print("3-1 = 2")
if number1 == 3 and operation == '-' and number2 == 2:
	print("3-2 = 1")
if number1 == 3 and operation == '-' and number2 == 3:
	print("3-3 = 0")
if number1 == 3 and operation == '-' and number2 == 4:
	print("3-4 = -1")
if number1 == 3 and operation == '-' and number2 == 5:
	print("3-5 = -2")
if number1 == 3 and operation == '-' and number2 == 6:
	print("3-6 = -3")
if number1 == 3 and operation == '-' and number2 == 7:
	print("3-7 = -4")
if number1 == 3 and operation == '-' and number2 == 8:
	print("3-8 = -5")
if number1 == 3 and operation == '-' and number2 == 9:
	print("3-9 = -6")
if number1 == 3 and operation == '-' and number2 == 10:
	print("3-10 = -7")
if number1 == 4 and operation == '-' and number2 == 0:
	print("4-0 = 4")
if number1 == 4 and operation == '-' and number2 == 1:
	print("4-1 = 3")
if number1 == 4 and operation == '-' and number2 == 2:
	print("4-2 = 2")
if number1 == 4 and operation == '-' and number2 == 3:
	print("4-3 = 1")
if number1 == 4 and operation == '-' and number2 == 4:
	print("4-4 = 0")
if number1 == 4 and operation == '-' and number2 == 5:
	print("4-5 = -1")
if number1 == 4 and operation == '-' and number2 == 6:
	print("4-6 = -2")
if number1 == 4 and operation == '-' and number2 == 7:
	print("4-7 = -3")
if number1 == 4 and operation == '-' and number2 == 8:
	print("4-8 = -4")
if number1 == 4 and operation == '-' and number2 == 9:
	print("4-9 = -5")
if number1 == 4 and operation == '-' and number2 == 10:
	print("4-10 = -6")
if number1 == 5 and operation == '-' and number2 == 0:
	print("5-0 = 5")
if number1 == 5 and operation == '-' and number2 == 1:
	print("5-1 = 4")
if number1 == 5 and operation == '-' and number2 == 2:
	print("5-2 = 3")
if number1 == 5 and operation == '-' and number2 == 3:
	print("5-3 = 2")
if number1 == 5 and operation == '-' and number2 == 4:
	print("5-4 = 1")
if number1 == 5 and operation == '-' and number2 == 5:
	print("5-5 = 0")
if number1 == 5 and operation == '-' and number2 == 6:
	print("5-6 = -1")
if number1 == 5 and operation == '-' and number2 == 7:
	print("5-7 = -2")
if number1 == 5 and operation == '-' and number2 == 8:
	print("5-8 = -3")
if number1 == 5 and operation == '-' and number2 == 9:
	print("5-9 = -4")
if number1 == 5 and operation == '-' and number2 == 10:
	print("5-10 = -5")
if number1 == 6 and operation == '-' and number2 == 0:
	print("6-0 = 6")
if number1 == 6 and operation == '-' and number2 == 1:
	print("6-1 = 5")
if number1 == 6 and operation == '-' and number2 == 2:
	print("6-2 = 4")
if number1 == 6 and operation == '-' and number2 == 3:
	print("6-3 = 3")
if number1 == 6 and operation == '-' and number2 == 4:
	print("6-4 = 2")
if number1 == 6 and operation == '-' and number2 == 5:
	print("6-5 = 1")
if number1 == 6 and operation == '-' and number2 == 6:
	print("6-6 = 0")
if number1 == 6 and operation == '-' and number2 == 7:
	print("6-7 = -1")
if number1 == 6 and operation == '-' and number2 == 8:
	print("6-8 = -2")
if number1 == 6 and operation == '-' and number2 == 9:
	print("6-9 = -3")
if number1 == 6 and operation == '-' and number2 == 10:
	print("6-10 = -4")
if number1 == 7 and operation == '-' and number2 == 0:
	print("7-0 = 7")
if number1 == 7 and operation == '-' and number2 == 1:
	print("7-1 = 6")
if number1 == 7 and operation == '-' and number2 == 2:
	print("7-2 = 5")
if number1 == 7 and operation == '-' and number2 == 3:
	print("7-3 = 4")
if number1 == 7 and operation == '-' and number2 == 4:
	print("7-4 = 3")
if number1 == 7 and operation == '-' and number2 == 5:
	print("7-5 = 2")
if number1 == 7 and operation == '-' and number2 == 6:
	print("7-6 = 1")
if number1 == 7 and operation == '-' and number2 == 7:
	print("7-7 = 0")
if number1 == 7 and operation == '-' and number2 == 8:
	print("7-8 = -1")
if number1 == 7 and operation == '-' and number2 == 9:
	print("7-9 = -2")
if number1 == 7 and operation == '-' and number2 == 10:
	print("7-10 = -3")
if number1 == 8 and operation == '-' and number2 == 0:
	print("8-0 = 8")
if number1 == 8 and operation == '-' and number2 == 1:
	print("8-1 = 7")
if number1 == 8 and operation == '-' and number2 == 2:
	print("8-2 = 6")
if number1 == 8 and operation == '-' and number2 == 3:
	print("8-3 = 5")
if number1 == 8 and operation == '-' and number2 == 4:
	print("8-4 = 4")
if number1 == 8 and operation == '-' and number2 == 5:
	print("8-5 = 3")
if number1 == 8 and operation == '-' and number2 == 6:
	print("8-6 = 2")
if number1 == 8 and operation == '-' and number2 == 7:
	print("8-7 = 1")
if number1 == 8 and operation == '-' and number2 == 8:
	print("8-8 = 0")
if number1 == 8 and operation == '-' and number2 == 9:
	print("8-9 = -1")
if number1 == 8 and operation == '-' and number2 == 10:
	print("8-10 = -2")
if number1 == 9 and operation == '-' and number2 == 0:
	print("9-0 = 9")
if number1 == 9 and operation == '-' and number2 == 1:
	print("9-1 = 8")
if number1 == 9 and operation == '-' and number2 == 2:
	print("9-2 = 7")
if number1 == 9 and operation == '-' and number2 == 3:
	print("9-3 = 6")
if number1 == 9 and operation == '-' and number2 == 4:
	print("9-4 = 5")
if number1 == 9 and operation == '-' and number2 == 5:
	print("9-5 = 4")
if number1 == 9 and operation == '-' and number2 == 6:
	print("9-6 = 3")
if number1 == 9 and operation == '-' and number2 == 7:
	print("9-7 = 2")
if number1 == 9 and operation == '-' and number2 == 8:
	print("9-8 = 1")
if number1 == 9 and operation == '-' and number2 == 9:
	print("9-9 = 0")
if number1 == 9 and operation == '-' and number2 == 10:
	print("9-10 = -1")
if number1 == 10 and operation == '-' and number2 == 0:
	print("10-0 = 10")
if number1 == 10 and operation == '-' and number2 == 1:
	print("10-1 = 9")
if number1 == 10 and operation == '-' and number2 == 2:
	print("10-2 = 8")
if number1 == 10 and operation == '-' and number2 == 3:
	print("10-3 = 7")
if number1 == 10 and operation == '-' and number2 == 4:
	print("10-4 = 6")
if number1 == 10 and operation == '-' and number2 == 5:
	print("10-5 = 5")
if number1 == 10 and operation == '-' and number2 == 6:
	print("10-6 = 4")
if number1 == 10 and operation == '-' and number2 == 7:
	print("10-7 = 3")
if number1 == 10 and operation == '-' and number2 == 8:
	print("10-8 = 2")
if number1 == 10 and operation == '-' and number2 == 9:
	print("10-9 = 1")
if number1 == 10 and operation == '-' and number2 == 10:
	print("10-10 = 0")
if number1 == 0 and operation == '*' and number2 == 0:
	print("0*0 = 0")
if number1 == 0 and operation == '*' and number2 == 1:
	print("0*1 = 0")
if number1 == 0 and operation == '*' and number2 == 2:
	print("0*2 = 0")
if number1 == 0 and operation == '*' and number2 == 3:
	print("0*3 = 0")
if number1 == 0 and operation == '*' and number2 == 4:
	print("0*4 = 0")
if number1 == 0 and operation == '*' and number2 == 5:
	print("0*5 = 0")
if number1 == 0 and operation == '*' and number2 == 6:
	print("0*6 = 0")
if number1 == 0 and operation == '*' and number2 == 7:
	print("0*7 = 0")
if number1 == 0 and operation == '*' and number2 == 8:
	print("0*8 = 0")
if number1 == 0 and operation == '*' and number2 == 9:
	print("0*9 = 0")
if number1 == 0 and operation == '*' and number2 == 10:
	print("0*10 = 0")
if number1 == 1 and operation == '*' and number2 == 0:
	print("1*0 = 0")
if number1 == 1 and operation == '*' and number2 == 1:
	print("1*1 = 1")
if number1 == 1 and operation == '*' and number2 == 2:
	print("1*2 = 2")
if number1 == 1 and operation == '*' and number2 == 3:
	print("1*3 = 3")
if number1 == 1 and operation == '*' and number2 == 4:
	print("1*4 = 4")
if number1 == 1 and operation == '*' and number2 == 5:
	print("1*5 = 5")
if number1 == 1 and operation == '*' and number2 == 6:
	print("1*6 = 6")
if number1 == 1 and operation == '*' and number2 == 7:
	print("1*7 = 7")
if number1 == 1 and operation == '*' and number2 == 8:
	print("1*8 = 8")
if number1 == 1 and operation == '*' and number2 == 9:
	print("1*9 = 9")
if number1 == 1 and operation == '*' and number2 == 10:
	print("1*10 = 10")
if number1 == 2 and operation == '*' and number2 == 0:
	print("2*0 = 0")
if number1 == 2 and operation == '*' and number2 == 1:
	print("2*1 = 2")
if number1 == 2 and operation == '*' and number2 == 2:
	print("2*2 = 4")
if number1 == 2 and operation == '*' and number2 == 3:
	print("2*3 = 6")
if number1 == 2 and operation == '*' and number2 == 4:
	print("2*4 = 8")
if number1 == 2 and operation == '*' and number2 == 5:
	print("2*5 = 10")
if number1 == 2 and operation == '*' and number2 == 6:
	print("2*6 = 12")
if number1 == 2 and operation == '*' and number2 == 7:
	print("2*7 = 14")
if number1 == 2 and operation == '*' and number2 == 8:
	print("2*8 = 16")
if number1 == 2 and operation == '*' and number2 == 9:
	print("2*9 = 18")
if number1 == 2 and operation == '*' and number2 == 10:
	print("2*10 = 20")
if number1 == 3 and operation == '*' and number2 == 0:
	print("3*0 = 0")
if number1 == 3 and operation == '*' and number2 == 1:
	print("3*1 = 3")
if number1 == 3 and operation == '*' and number2 == 2:
	print("3*2 = 6")
if number1 == 3 and operation == '*' and number2 == 3:
	print("3*3 = 9")
if number1 == 3 and operation == '*' and number2 == 4:
	print("3*4 = 12")
if number1 == 3 and operation == '*' and number2 == 5:
	print("3*5 = 15")
if number1 == 3 and operation == '*' and number2 == 6:
	print("3*6 = 18")
if number1 == 3 and operation == '*' and number2 == 7:
	print("3*7 = 21")
if number1 == 3 and operation == '*' and number2 == 8:
	print("3*8 = 24")
if number1 == 3 and operation == '*' and number2 == 9:
	print("3*9 = 27")
if number1 == 3 and operation == '*' and number2 == 10:
	print("3*10 = 30")
if number1 == 4 and operation == '*' and number2 == 0:
	print("4*0 = 0")
if number1 == 4 and operation == '*' and number2 == 1:
	print("4*1 = 4")
if number1 == 4 and operation == '*' and number2 == 2:
	print("4*2 = 8")
if number1 == 4 and operation == '*' and number2 == 3:
	print("4*3 = 12")
if number1 == 4 and operation == '*' and number2 == 4:
	print("4*4 = 16")
if number1 == 4 and operation == '*' and number2 == 5:
	print("4*5 = 20")
if number1 == 4 and operation == '*' and number2 == 6:
	print("4*6 = 24")
if number1 == 4 and operation == '*' and number2 == 7:
	print("4*7 = 28")
if number1 == 4 and operation == '*' and number2 == 8:
	print("4*8 = 32")
if number1 == 4 and operation == '*' and number2 == 9:
	print("4*9 = 36")
if number1 == 4 and operation == '*' and number2 == 10:
	print("4*10 = 40")
if number1 == 5 and operation == '*' and number2 == 0:
	print("5*0 = 0")
if number1 == 5 and operation == '*' and number2 == 1:
	print("5*1 = 5")
if number1 == 5 and operation == '*' and number2 == 2:
	print("5*2 = 10")
if number1 == 5 and operation == '*' and number2 == 3:
	print("5*3 = 15")
if number1 == 5 and operation == '*' and number2 == 4:
	print("5*4 = 20")
if number1 == 5 and operation == '*' and number2 == 5:
	print("5*5 = 25")
if number1 == 5 and operation == '*' and number2 == 6:
	print("5*6 = 30")
if number1 == 5 and operation == '*' and number2 == 7:
	print("5*7 = 35")
if number1 == 5 and operation == '*' and number2 == 8:
	print("5*8 = 40")
if number1 == 5 and operation == '*' and number2 == 9:
	print("5*9 = 45")
if number1 == 5 and operation == '*' and number2 == 10:
	print("5*10 = 50")
if number1 == 6 and operation == '*' and number2 == 0:
	print("6*0 = 0")
if number1 == 6 and operation == '*' and number2 == 1:
	print("6*1 = 6")
if number1 == 6 and operation == '*' and number2 == 2:
	print("6*2 = 12")
if number1 == 6 and operation == '*' and number2 == 3:
	print("6*3 = 18")
if number1 == 6 and operation == '*' and number2 == 4:
	print("6*4 = 24")
if number1 == 6 and operation == '*' and number2 == 5:
	print("6*5 = 30")
if number1 == 6 and operation == '*' and number2 == 6:
	print("6*6 = 36")
if number1 == 6 and operation == '*' and number2 == 7:
	print("6*7 = 42")
if number1 == 6 and operation == '*' and number2 == 8:
	print("6*8 = 48")
if number1 == 6 and operation == '*' and number2 == 9:
	print("6*9 = 54")
if number1 == 6 and operation == '*' and number2 == 10:
	print("6*10 = 60")
if number1 == 7 and operation == '*' and number2 == 0:
	print("7*0 = 0")
if number1 == 7 and operation == '*' and number2 == 1:
	print("7*1 = 7")
if number1 == 7 and operation == '*' and number2 == 2:
	print("7*2 = 14")
if number1 == 7 and operation == '*' and number2 == 3:
	print("7*3 = 21")
if number1 == 7 and operation == '*' and number2 == 4:
	print("7*4 = 28")
if number1 == 7 and operation == '*' and number2 == 5:
	print("7*5 = 35")
if number1 == 7 and operation == '*' and number2 == 6:
	print("7*6 = 42")
if number1 == 7 and operation == '*' and number2 == 7:
	print("7*7 = 49")
if number1 == 7 and operation == '*' and number2 == 8:
	print("7*8 = 56")
if number1 == 7 and operation == '*' and number2 == 9:
	print("7*9 = 63")
if number1 == 7 and operation == '*' and number2 == 10:
	print("7*10 = 70")
if number1 == 8 and operation == '*' and number2 == 0:
	print("8*0 = 0")
if number1 == 8 and operation == '*' and number2 == 1:
	print("8*1 = 8")
if number1 == 8 and operation == '*' and number2 == 2:
	print("8*2 = 16")
if number1 == 8 and operation == '*' and number2 == 3:
	print("8*3 = 24")
if number1 == 8 and operation == '*' and number2 == 4:
	print("8*4 = 32")
if number1 == 8 and operation == '*' and number2 == 5:
	print("8*5 = 40")
if number1 == 8 and operation == '*' and number2 == 6:
	print("8*6 = 48")
if number1 == 8 and operation == '*' and number2 == 7:
	print("8*7 = 56")
if number1 == 8 and operation == '*' and number2 == 8:
	print("8*8 = 64")
if number1 == 8 and operation == '*' and number2 == 9:
	print("8*9 = 72")
if number1 == 8 and operation == '*' and number2 == 10:
	print("8*10 = 80")
if number1 == 9 and operation == '*' and number2 == 0:
	print("9*0 = 0")
if number1 == 9 and operation == '*' and number2 == 1:
	print("9*1 = 9")
if number1 == 9 and operation == '*' and number2 == 2:
	print("9*2 = 18")
if number1 == 9 and operation == '*' and number2 == 3:
	print("9*3 = 27")
if number1 == 9 and operation == '*' and number2 == 4:
	print("9*4 = 36")
if number1 == 9 and operation == '*' and number2 == 5:
	print("9*5 = 45")
if number1 == 9 and operation == '*' and number2 == 6:
	print("9*6 = 54")
if number1 == 9 and operation == '*' and number2 == 7:
	print("9*7 = 63")
if number1 == 9 and operation == '*' and number2 == 8:
	print("9*8 = 72")
if number1 == 9 and operation == '*' and number2 == 9:
	print("9*9 = 81")
if number1 == 9 and operation == '*' and number2 == 10:
	print("9*10 = 90")
if number1 == 10 and operation == '*' and number2 == 0:
	print("10*0 = 0")
if number1 == 10 and operation == '*' and number2 == 1:
	print("10*1 = 10")
if number1 == 10 and operation == '*' and number2 == 2:
	print("10*2 = 20")
if number1 == 10 and operation == '*' and number2 == 3:
	print("10*3 = 30")
if number1 == 10 and operation == '*' and number2 == 4:
	print("10*4 = 40")
if number1 == 10 and operation == '*' and number2 == 5:
	print("10*5 = 50")
if number1 == 10 and operation == '*' and number2 == 6:
	print("10*6 = 60")
if number1 == 10 and operation == '*' and number2 == 7:
	print("10*7 = 70")
if number1 == 10 and operation == '*' and number2 == 8:
	print("10*8 = 80")
if number1 == 10 and operation == '*' and number2 == 9:
	print("10*9 = 90")
if number1 == 10 and operation == '*' and number2 == 10:
	print("10*10 = 100")
if number1 == 0 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 0 and operation == '/' and number2 == 1:
	print("0/1 = 0.0")
if number1 == 0 and operation == '/' and number2 == 2:
	print("0/2 = 0.0")
if number1 == 0 and operation == '/' and number2 == 3:
	print("0/3 = 0.0")
if number1 == 0 and operation == '/' and number2 == 4:
	print("0/4 = 0.0")
if number1 == 0 and operation == '/' and number2 == 5:
	print("0/5 = 0.0")
if number1 == 0 and operation == '/' and number2 == 6:
	print("0/6 = 0.0")
if number1 == 0 and operation == '/' and number2 == 7:
	print("0/7 = 0.0")
if number1 == 0 and operation == '/' and number2 == 8:
	print("0/8 = 0.0")
if number1 == 0 and operation == '/' and number2 == 9:
	print("0/9 = 0.0")
if number1 == 0 and operation == '/' and number2 == 10:
	print("0/10 = 0.0")
if number1 == 1 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 1 and operation == '/' and number2 == 1:
	print("1/1 = 1.0")
if number1 == 1 and operation == '/' and number2 == 2:
	print("1/2 = 0.5")
if number1 == 1 and operation == '/' and number2 == 3:
	print("1/3 = 0.3333333333333333")
if number1 == 1 and operation == '/' and number2 == 4:
	print("1/4 = 0.25")
if number1 == 1 and operation == '/' and number2 == 5:
	print("1/5 = 0.2")
if number1 == 1 and operation == '/' and number2 == 6:
	print("1/6 = 0.16666666666666666")
if number1 == 1 and operation == '/' and number2 == 7:
	print("1/7 = 0.14285714285714285")
if number1 == 1 and operation == '/' and number2 == 8:
	print("1/8 = 0.125")
if number1 == 1 and operation == '/' and number2 == 9:
	print("1/9 = 0.1111111111111111")
if number1 == 1 and operation == '/' and number2 == 10:
	print("1/10 = 0.1")
if number1 == 2 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 2 and operation == '/' and number2 == 1:
	print("2/1 = 2.0")
if number1 == 2 and operation == '/' and number2 == 2:
	print("2/2 = 1.0")
if number1 == 2 and operation == '/' and number2 == 3:
	print("2/3 = 0.6666666666666666")
if number1 == 2 and operation == '/' and number2 == 4:
	print("2/4 = 0.5")
if number1 == 2 and operation == '/' and number2 == 5:
	print("2/5 = 0.4")
if number1 == 2 and operation == '/' and number2 == 6:
	print("2/6 = 0.3333333333333333")
if number1 == 2 and operation == '/' and number2 == 7:
	print("2/7 = 0.2857142857142857")
if number1 == 2 and operation == '/' and number2 == 8:
	print("2/8 = 0.25")
if number1 == 2 and operation == '/' and number2 == 9:
	print("2/9 = 0.2222222222222222")
if number1 == 2 and operation == '/' and number2 == 10:
	print("2/10 = 0.2")
if number1 == 3 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 3 and operation == '/' and number2 == 1:
	print("3/1 = 3.0")
if number1 == 3 and operation == '/' and number2 == 2:
	print("3/2 = 1.5")
if number1 == 3 and operation == '/' and number2 == 3:
	print("3/3 = 1.0")
if number1 == 3 and operation == '/' and number2 == 4:
	print("3/4 = 0.75")
if number1 == 3 and operation == '/' and number2 == 5:
	print("3/5 = 0.6")
if number1 == 3 and operation == '/' and number2 == 6:
	print("3/6 = 0.5")
if number1 == 3 and operation == '/' and number2 == 7:
	print("3/7 = 0.42857142857142855")
if number1 == 3 and operation == '/' and number2 == 8:
	print("3/8 = 0.375")
if number1 == 3 and operation == '/' and number2 == 9:
	print("3/9 = 0.3333333333333333")
if number1 == 3 and operation == '/' and number2 == 10:
	print("3/10 = 0.3")
if number1 == 4 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 4 and operation == '/' and number2 == 1:
	print("4/1 = 4.0")
if number1 == 4 and operation == '/' and number2 == 2:
	print("4/2 = 2.0")
if number1 == 4 and operation == '/' and number2 == 3:
	print("4/3 = 1.3333333333333333")
if number1 == 4 and operation == '/' and number2 == 4:
	print("4/4 = 1.0")
if number1 == 4 and operation == '/' and number2 == 5:
	print("4/5 = 0.8")
if number1 == 4 and operation == '/' and number2 == 6:
	print("4/6 = 0.6666666666666666")
if number1 == 4 and operation == '/' and number2 == 7:
	print("4/7 = 0.5714285714285714")
if number1 == 4 and operation == '/' and number2 == 8:
	print("4/8 = 0.5")
if number1 == 4 and operation == '/' and number2 == 9:
	print("4/9 = 0.4444444444444444")
if number1 == 4 and operation == '/' and number2 == 10:
	print("4/10 = 0.4")
if number1 == 5 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 5 and operation == '/' and number2 == 1:
	print("5/1 = 5.0")
if number1 == 5 and operation == '/' and number2 == 2:
	print("5/2 = 2.5")
if number1 == 5 and operation == '/' and number2 == 3:
	print("5/3 = 1.6666666666666667")
if number1 == 5 and operation == '/' and number2 == 4:
	print("5/4 = 1.25")
if number1 == 5 and operation == '/' and number2 == 5:
	print("5/5 = 1.0")
if number1 == 5 and operation == '/' and number2 == 6:
	print("5/6 = 0.8333333333333334")
if number1 == 5 and operation == '/' and number2 == 7:
	print("5/7 = 0.7142857142857143")
if number1 == 5 and operation == '/' and number2 == 8:
	print("5/8 = 0.625")
if number1 == 5 and operation == '/' and number2 == 9:
	print("5/9 = 0.5555555555555556")
if number1 == 5 and operation == '/' and number2 == 10:
	print("5/10 = 0.5")
if number1 == 6 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 6 and operation == '/' and number2 == 1:
	print("6/1 = 6.0")
if number1 == 6 and operation == '/' and number2 == 2:
	print("6/2 = 3.0")
if number1 == 6 and operation == '/' and number2 == 3:
	print("6/3 = 2.0")
if number1 == 6 and operation == '/' and number2 == 4:
	print("6/4 = 1.5")
if number1 == 6 and operation == '/' and number2 == 5:
	print("6/5 = 1.2")
if number1 == 6 and operation == '/' and number2 == 6:
	print("6/6 = 1.0")
if number1 == 6 and operation == '/' and number2 == 7:
	print("6/7 = 0.8571428571428571")
if number1 == 6 and operation == '/' and number2 == 8:
	print("6/8 = 0.75")
if number1 == 6 and operation == '/' and number2 == 9:
	print("6/9 = 0.6666666666666666")
if number1 == 6 and operation == '/' and number2 == 10:
	print("6/10 = 0.6")
if number1 == 7 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 7 and operation == '/' and number2 == 1:
	print("7/1 = 7.0")
if number1 == 7 and operation == '/' and number2 == 2:
	print("7/2 = 3.5")
if number1 == 7 and operation == '/' and number2 == 3:
	print("7/3 = 2.3333333333333335")
if number1 == 7 and operation == '/' and number2 == 4:
	print("7/4 = 1.75")
if number1 == 7 and operation == '/' and number2 == 5:
	print("7/5 = 1.4")
if number1 == 7 and operation == '/' and number2 == 6:
	print("7/6 = 1.1666666666666667")
if number1 == 7 and operation == '/' and number2 == 7:
	print("7/7 = 1.0")
if number1 == 7 and operation == '/' and number2 == 8:
	print("7/8 = 0.875")
if number1 == 7 and operation == '/' and number2 == 9:
	print("7/9 = 0.7777777777777778")
if number1 == 7 and operation == '/' and number2 == 10:
	print("7/10 = 0.7")
if number1 == 8 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 8 and operation == '/' and number2 == 1:
	print("8/1 = 8.0")
if number1 == 8 and operation == '/' and number2 == 2:
	print("8/2 = 4.0")
if number1 == 8 and operation == '/' and number2 == 3:
	print("8/3 = 2.6666666666666665")
if number1 == 8 and operation == '/' and number2 == 4:
	print("8/4 = 2.0")
if number1 == 8 and operation == '/' and number2 == 5:
	print("8/5 = 1.6")
if number1 == 8 and operation == '/' and number2 == 6:
	print("8/6 = 1.3333333333333333")
if number1 == 8 and operation == '/' and number2 == 7:
	print("8/7 = 1.1428571428571428")
if number1 == 8 and operation == '/' and number2 == 8:
	print("8/8 = 1.0")
if number1 == 8 and operation == '/' and number2 == 9:
	print("8/9 = 0.8888888888888888")
if number1 == 8 and operation == '/' and number2 == 10:
	print("8/10 = 0.8")
if number1 == 9 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 9 and operation == '/' and number2 == 1:
	print("9/1 = 9.0")
if number1 == 9 and operation == '/' and number2 == 2:
	print("9/2 = 4.5")
if number1 == 9 and operation == '/' and number2 == 3:
	print("9/3 = 3.0")
if number1 == 9 and operation == '/' and number2 == 4:
	print("9/4 = 2.25")
if number1 == 9 and operation == '/' and number2 == 5:
	print("9/5 = 1.8")
if number1 == 9 and operation == '/' and number2 == 6:
	print("9/6 = 1.5")
if number1 == 9 and operation == '/' and number2 == 7:
	print("9/7 = 1.2857142857142858")
if number1 == 9 and operation == '/' and number2 == 8:
	print("9/8 = 1.125")
if number1 == 9 and operation == '/' and number2 == 9:
	print("9/9 = 1.0")
if number1 == 9 and operation == '/' and number2 == 10:
	print("9/10 = 0.9")
if number1 == 10 and operation == '/' and number2 == 0:
	print("Cannot divide by Zero.")
if number1 == 10 and operation == '/' and number2 == 1:
	print("10/1 = 10.0")
if number1 == 10 and operation == '/' and number2 == 2:
	print("10/2 = 5.0")
if number1 == 10 and operation == '/' and number2 == 3:
	print("10/3 = 3.3333333333333335")
if number1 == 10 and operation == '/' and number2 == 4:
	print("10/4 = 2.5")
if number1 == 10 and operation == '/' and number2 == 5:
	print("10/5 = 2.0")
if number1 == 10 and operation == '/' and number2 == 6:
	print("10/6 = 1.6666666666666667")
if number1 == 10 and operation == '/' and number2 == 7:
	print("10/7 = 1.4285714285714286")
if number1 == 10 and operation == '/' and number2 == 8:
	print("10/8 = 1.25")
if number1 == 10 and operation == '/' and number2 == 9:
	print("10/9 = 1.1111111111111112")
if number1 == 10 and operation == '/' and number2 == 10:
	print("10/10 = 1.0")

print("\nCheckout the original code by AceLewis on GitHub.\nHave a good day!")