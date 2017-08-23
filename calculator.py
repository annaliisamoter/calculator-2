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
        numbers_strings = output[1:]
        numbers = []
        for num in numbers_strings:
            numbers.append(int(num))

    # if len(output) > 1:
    #     num1 = int(output[1])

    # if len(output) > 2:
    #     num2 = int(output[2])

    # if len(output) > 3:
    #     num3 = int(output[3])

    if command == 'q' or command == 'quit':
        break

    elif command == '+':
        print add(numbers)

    elif command == '-':
        print subtract(numbers)

    elif command == '*':
        print multiply(numbers)

    elif command == '/':
        print divide(numbers)

    elif command == 'square':
        print square(numbers)

    elif command == 'cube':
        print cube(numbers)

    elif command == 'pow':
        print power(numbers)

    elif command == 'mod':
        print mod(numbers)

    elif command == 'x+':
        print add_mult(numbers)

    elif command == 'cubes+':
        print add_cubes(numbers)

    else:
        print "That's not a valid entry! Please try again."
