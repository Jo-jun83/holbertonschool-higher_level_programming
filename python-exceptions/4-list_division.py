#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides elements of two lists element by element.

    Args:
        my_list_1 (list): The first list of numbers.
        my_list_2 (list): The second list of numbers.
        list_length (int): The number of elements to divide.

    Returns:
        list: A new list containing the division results. If an
        error occurs during division, the result for that element
        will be 0 and an appropriate message will be printed.

    Raises:
        TypeError: If elements in the lists are not numbers.
        ZeroDivisionError: If an element in my_list_2 is zero.
        IndexError: If an index is out of range for either list.
    """
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result
