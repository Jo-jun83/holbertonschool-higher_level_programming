#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two numbers and prints the result.

    This function takes two arguments, `a` and `b`, attempts to divide `a` by `b`, 
    and prints the result of the division. If the division is successful, it returns 
    the result. If a division by zero occurs, it prints a message and returns None.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or None: The result of the division if successful, otherwise None.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result


    