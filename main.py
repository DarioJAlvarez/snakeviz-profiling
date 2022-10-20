import random
import string
import sys
from copy import deepcopy


def generate_random_string(size: int = 10) -> str:
    """
    Generate a random string of a given size.

    :param size: str Length string to be generated.
    :return: String of desired size
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))


def order_dict_by_key(dictionary: dict) -> dict:
    """
    Orders a dict alphabetically by keys.

    :param dictionary: dict Dictionary to be ordered.
    :return: Ordered dict by keys.
    """
    new_dict = {}
    for key in sorted(dictionary.keys()):
        new_dict[key] = dictionary[key]
    return new_dict


def order_dict_by_value(dictionary: dict) -> dict:
    """
    Orders a dict by values, then orders it alphabetically.
    Not a good implementation but ok for profiling.

    :param dictionary: dict Dictionary to be ordered
    :return: Ordered dict by values, then by keys.
    """
    values = set(dictionary.values())
    list_of_dicts = []
    for value in sorted(values):
        subset = {key: value for key, value_ in dictionary.items() if value_ == value}
        # Append deepcopy, just for making this function slower
        list_of_dicts.append(order_dict_by_key(deepcopy(subset)))
    new_dict = {}
    for dict_ in list_of_dicts:
        new_dict = {**new_dict, **dict_}
    return new_dict


def main_function_to_be_analysed(list_size: int = 10):
    """
    Does stuff to be analysed by profiling tool:
        - Creates two list of equal size. One of numbers and another of string.
        - Creates a dictionary from these lists.
        - Orders this dictionary by keys.
        - Order this dictionary by values and keys.
    
    :param list_size: int Size of the lists to be generated.
    """
    numbers_list = [random.randint(0, 9) for _ in range(list_size)]
    strings_list = [generate_random_string() for _ in range(list_size)]
    dictionary = dict(zip(strings_list, numbers_list))
    order_dict_by_key(dictionary)
    order_dict_by_value(dictionary)
 

if __name__ == "__main__":
    try:
        size = int(sys.argv[1])
    except IndexError:
        size = 10
    main_function_to_be_analysed(size)
