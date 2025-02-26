"""
Module app
This module provides simple arithmetic operations and greeting functions.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def multiply(x, y):
    """
    Multiply two numbers.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide x by y.

    Parameters:
    x (int or float): The numerator.
    y (int or float): The denominator.

    Returns:
    float or None: The result of x divided by y if y is not zero, otherwise None.
    """
    if y != 0:
        return x / y
    # Return None explicitly if division by zero occurs
    return None

def greet(name):
    """
    Greet a person by name.

    Parameters:
    name (str): The name of the person. If empty, defaults to 'World'.

    Returns:
    str: A greeting message.
    """
    if name == "":
        return "Hello, World!"
    return "Hello, " + name
