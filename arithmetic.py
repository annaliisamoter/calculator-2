"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the input integers."""
    total = 0
    for num in numbers:
        total += int(num)
    return total


def subtract(numbers):
    """Return the second number subtracted from the first."""
    total = int(numbers[0])
    if len(numbers) > 1:
        new_numbers = numbers[1:]
        for num in new_numbers:
            total = total - num
    return total


def multiply(num1, num2):
    """Multiply the two inputs together."""
    return int(num1 * num2)


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""
    return float(num1)/num2


def square(num1):
    """Return the square of the input."""
    return int(num1 * num1)


def cube(num1):
    """Return the cube of the input."""
    return int(num1 * num1 * num1)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return int(num1 ** num2)


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return int(num1 % num2)


def add_mult(num1, num2, num3):
    """Add first two inputs and multiply sum with third"""
    return int((num1 + num2) * num3)


def add_cubes(num1, num2):
    """Cubes both inputs and returns sum"""
    return int((num1 ** 3) + (num2 ** 3))
