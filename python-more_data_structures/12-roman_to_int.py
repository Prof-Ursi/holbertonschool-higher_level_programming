#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_converted = 0
    roman_previous = 0
    roman_character = 'I'

    for roman_character in roman_string:
        roman_current = roman_numbers.get(roman_character, 0)
        if roman_current > roman_previous:
            roman_converted += roman_current - 2 * roman_previous
        else:
            roman_converted += roman_current
        roman_previous = roman_current
    if not (1 <= roman_converted <= 3999):
        return 0
    return roman_converted
