"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the input integers."""
    total = 0
    for num in numbers:
        total += num
    return total


def subtract(numbers):
    """Return the total of integers subracted from the first."""
    total = numbers[0]
    if len(numbers) > 1:
        new_numbers = numbers[1:]
        for num in new_numbers:
            total = total - num
    return total


def multiply(numbers):
    """Multiply all inputs together."""
    total = 1
    for num in numbers:
        total = total * num
    return total


def divide(numbers):
    """Divide the first input by the all of the following, returning a float."""
    total = float(numbers[0])
    if len(numbers) > 1:
        new_numbers = numbers[1:]
        for num in new_numbers:
            total = total / num
    return total


def square(numbers):
    """Return the square of the input."""
    return numbers[0] * numbers[0]


def cube(numbers):
    """Return the cube of the input."""
    return numbers[0] * numbers[0] * numbers[0]


def power(numbers):
    """Raise the first number to the power of the second number and return the value."""
    if len(numbers) != 2:
        return "You need exactly 2 numbers to make this function work."
    return numbers[0] ** numbers[1]


def mod(numbers):
    """Return the remainder of first number divided by second number."""
    if len(numbers) != 2:
        return "You need exactly 2 numbers to make this function work."
    return numbers[0] % numbers[1]


def add_mult(numbers):
    """Add first two inputs and multiply sum with third"""
    if len(numbers) != 3:
        return "You need exactly 3 numbers to make this function work."
    return (numbers[0] + numbers[1]) * numbers[2]


def add_cubes(numbers):
    """Cubes both inputs and returns sum"""
    return (numbers[0] ** 3) + (numbers[1] ** 3)
