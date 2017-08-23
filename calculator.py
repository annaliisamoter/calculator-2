"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# No setup

while True:
    input = raw_input("> ")
    output = input.split(" ")

    command = output[0]
    num1 = int(output[1])
    num2 = int(output[2])

    if command == 'q' or command == 'quit':
        break
    elif command == '+':
        print add(num1, num2)
#repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token
