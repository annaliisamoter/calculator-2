"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    input = raw_input("> ")
    output = input.split(" ")

    command = output[0]
    if len(output) > 1:
        num1 = int(output[1])

    if len(output) > 2:
        num2 = int(output[2])

    if len(output) > 3:
        num3 = int(output[3])

    if command == 'q' or command == 'quit':
        break

    elif command == '+':
        print add(num1, num2)

    elif command == '-':
        print subtract(num1, num2)

    elif command == '*':
        print multiply(num1, num2)

    elif command == '/':
        print divide(num1, num2)

    elif command == 'square':
        print square(num1)

    elif command == 'cube':
        print cube(num1)

    elif command == 'pow':
        print power(num1, num2)

    elif command == 'mod':
        print mod(num1, num2)

    elif command == 'x+':
        print add_mult(num1, num2, num3)

    elif command == 'cubes+':
        print add_cubes(num1, num2)
