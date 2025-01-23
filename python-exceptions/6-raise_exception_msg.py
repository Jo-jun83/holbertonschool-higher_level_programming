#!/usr/bin/python3

def raise_exception_msg(message=""):
    """
    Raises a NameError exception with the provided message.

    Args:
        message (str): The message to be included in the NameError exception.
        Defaults to an empty string.

    Raises:
        NameError: An exception with the provided message.
    """
    raise NameError(message)
