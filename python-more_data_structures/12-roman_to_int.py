#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    total = 0
    i = 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    while i < len(roman_string):

        current_value = values[roman_string[i]]

        if i + 1 < len(roman_string):
            next_value = values[roman_string[i + 1]]
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

        i += 1

    return total
