#!/usr/bin/python3

"""
   fonction that print my name 
"""

def say_my_name(first_name, last_name=""):
    """
    Say_my_name

    Args:
        first_name (_type_): _description_
        last_name (str, optional): _description_. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    
    if not isinstance(first_name, str ):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str ):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
