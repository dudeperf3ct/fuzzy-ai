"""
calc_func.py contains math functions
"""


def add(a, b):
    """Add two numbers together

    Parameters
    ----------
    a : float
        First Operand
    b : float
        Second Operand

    Returns
    -------
    float
        Result of addition
    """
    return a + b


def subtract(a, b):
    """Subtract two numbers where order matters
    a is first operand and b is second operand

    Parameters
    ----------
    a : float
        First Operand
    b : float
        Second Operand

    Returns
    -------
    float
        Result of subtraction
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers

    Parameters
    ----------
    a : float
        First Operand
    b : float
        Second Operand

    Returns
    -------
    int
        Result of multiplication
    """
    return a * b


def divide(a, b):
    """Divide two numbers where order matters
    a is numerator and b is the denominator

    Parameters
    ----------
    a : float
        Numerator
    b : float
        Denominator

    Returns
    -------
    float
        Result of division

    Raises
    -------
    ZeroDivisionError
        If b is zero
    """
    try:
        return a * 1.0 / b
    except ZeroDivisionError:
        return None


def modulo(a, b):
    """Modulo two numbers where order matters
    a is numerator and b is the denominator

    Parameters
    ----------
    a : float
        Numerator
    b : float
        Denominator

    Returns
    -------
    float
        Result of modulo

    Raises
    -------
    ZeroDivisionError
        If b is zero
    """
    try:
        return a % b
    except ZeroDivisionError:
        return None
