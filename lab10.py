#zadnie 1
def is_palindrome(some_str: str) -> bool:
    return some_str == some_str[::-1]

#zadnie 2
def Caesar_Cipher(string_to_encrypt: str, key: int) -> str:
    encrypted_string = list(string_to_encrypt)
    for i, char in enumerate(string_to_encrypt):
        ascii_code = ord(char)
        new_ascii = ascii_code + key
        if 97 <= ascii_code <= 122:
            if new_ascii > 122:
                new_ascii = 96 + abs(122 - new_ascii)
        elif 65 < ascii_code < 90:
            if new_ascii > 90:
                new_ascii = 64 + abs(90 - new_ascii)
        else:
            continue
        encrypted_string[i] = chr(new_ascii)
    return ''.join(encrypted_string)

def encrypt_only_upper_letters_using_caesar(string_to_encrypt: str, key: int):
    encrypted_string = [
        Caesar_Cipher(i, key) if i.isupper() else i for i in string_to_encrypt]
    encrypted_string_func = list(
        map(
            lambda x: Caesar_Cipher(x, key)
            if x.isupper() else x, string_to_encrypt
            )
        )
    return ''.join(encrypted_string)

#zadnie 3
import random
import string

def generate_car_number(number_base: str = 'LU') -> str:
    elem_for_choice = [str(i) for i in range(10)] + list(
        string.ascii_uppercase
        )
    car_number = [random.choice(elem_for_choice) for _ in range(5)]
    return f'{number_base} {"".join(car_number)}'

#zadnie 4
def roman_to_arabic_conversion(num_in_roman: str) -> int:
    num_in_arabic = 0
    roman_arabic = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
        }
    for roman in num_in_roman:
        try:
            num_in_arabic += roman_arabic[roman]
        except KeyError:
            raise ValueError(f'Passed invalid num in roman format: {num_in_roman}')
    return num_in_arabic
