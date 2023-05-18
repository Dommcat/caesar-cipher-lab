
from english_words import get_english_words_set

import re

def encrypt(text, shift):
    encrypted_text = ''

    while shift > 26:
        shift -= 26

    for char in text:
        ascii_num = ord(char)
        shifted = False

        if ascii_num < 65 or ascii_num > 122:
            encrypted_text += char
            shifted = True

        elif 90 < ascii_num < 97:
            encrypted_text += char
            shifted = True

        if 96 < ascii_num < 123:
            ascii_num += shift
            if ascii_num > 122:
                ascii_num -= 26
            encrypted_text += chr(ascii_num)

        if 64 < ascii_num < 91:
            ascii_num += shift
            if ascii_num > 90:
                ascii_num -= 26
            encrypted_text += chr(ascii_num)

    return encrypted_text

def decrypt(text,shift):
    decrypted_text = ''

    while shift > 26:
        shift -= 26

    for char in text:
        ascii_num = ord(char)
        shifted = False

        if ascii_num < 65 or ascii_num > 122:
            decrypted_text += char
            shifted = True

        elif 90 < ascii_num < 97:
            decrypted_text += char
            shifted = True

        if 96 < ascii_num < 123:
            ascii_num -= shift
            if ascii_num < 97:
                ascii_num += 26
            decrypted_text += chr(ascii_num)

        if 64 < ascii_num < 91:
            ascii_num -= shift
            if ascii_num < 65:
                ascii_num += 26
            decrypted_text += chr(ascii_num)

    return decrypted_text

def crack(encrypted_text):
    decrypted_text = ''
    dictionary = get_english_words_set(['web2'], lower=True)
    final_shift = 0

    for shift in range(1, 26):

        decrypted_text = decrypt(encrypted_text, shift)

        words = decrypted_text.split()

        good_phrase = True

        for word in words:

            temp_word = remove_punctuation(word)

            if temp_word.lower() not in dictionary:
                good_phrase = False

        if good_phrase is True:
    
            return decrypted_text

    return ''

def remove_punctuation(text):
    # from https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', text)

    if __name__ == '__main__':
        phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
        print(f'Original: {phrase}')

        cracked = crack(phrase)
        print(f'Cracked: {cracked}')



































