"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def is_all_nums(numbers_strings):
    """Checks that inputs after the command are numbers."""
    for num in numbers_strings:
        try:
            num = int(num)
        except ValueError:
            print "You must enter numbers after the command. Please try again."
            return False
    return True


def run_command(command):
    """Validates and runs calculator commands."""
    if command == '+':
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
        print "That's not a valid command! Please try again."


while True:
    input = raw_input("> ").rstrip()
    output = input.split(" ")

    command = output[0]

    if command == 'q' or command == 'quit':
        break

    if len(output) <= 1:
        print "We need at least one number to run a function."

    if len(output) >= 2:
        numbers_strings = output[1:]

        if is_all_nums(numbers_strings) is True:
            numbers = []
            for num in numbers_strings:
                numbers.append(int(num))

            run_command(command)
