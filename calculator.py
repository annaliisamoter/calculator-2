"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# def validate_output(output):
#     # for item in output[1:]:
#     #     if item.isdigit() != True:
#     #         print "That is not a valid entry! Please try again."
#     if output == '+':
#         return False
#     return True


while True:
    input = raw_input("> ").rstrip()
    output = input.split(" ")

    command = output[0]
   # validate_output(output) is False:
        #print "Invalid entry. Please try again."

    if len(output) > 1:
        numbers_strings = output[1:]

        is_all_nums = True
        for num in numbers_strings:
            try:
                num = int(num)
            except ValueError:
                print "You must enter numbers after the command. Please try again."
                is_all_nums = False
                break

        if is_all_nums is True:
            numbers = []
            for num in numbers_strings:
                numbers.append(int(num))

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

    if command == 'q' or command == 'quit':
                break
