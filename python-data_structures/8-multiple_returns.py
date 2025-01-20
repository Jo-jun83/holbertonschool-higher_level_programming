#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a given sentence and
    its first character.

    If the sentence is empty, the first character should be None.

    Args:
        sentence (str): The sentence from which to extract the
        length and first character.

    Returns:
        tuple: A tuple containing the length of the sentence and
        its first character.
    """
    length = len(sentence)
    if length == 0:
        return (length, None)
    first = sentence[0]
    return (length, first)
