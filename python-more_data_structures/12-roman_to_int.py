#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string to convert.

    Returns:
        int: The integer representation of the Roman numeral.
        Returns 0 if the input is not a valid Roman numeral string.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        value = roman_values.get(char, 0)
        if value == 0:
            return 0  # Retourne 0 si caractère invalide

        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
