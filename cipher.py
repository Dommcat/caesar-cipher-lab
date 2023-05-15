# import string
from english_words import word_list, namelist
import string

def encrypt(text, shift) -> str:
    encrypted_text =''

    """
    Encrypts the given plain text phrase by shifting each letter in the phrase
    by the specified numeric shift. Shifts that exceed 26 wrap around, and shifts
    that push a letter out of range also wrap around.
    
    :param phrase: The plain text phrase to be encrypted.
    :param shift: The numeric shift used for encryption.
    :return: The encrypted string.
    """
    while shift > 26:
        shift -= 26

    for char in text:
        # convert to ascii number
        ascii_num = ord(char)
        shifted = False

        # if weird ascii number, don't shift and return same character
        if ascii_num < 65 or ascii_num > 122:
            encrypted_text += char
            shifted = True

        elif 90 < ascii_num < 97:
            encrypted_text += char
            shifted = True

        # lower case character
        if 96 < ascii_num < 123:
            ascii_num += shift
            if ascii_num > 122:
                ascii_num -= 26
            encrypted_text += chr(ascii_num)

        # upper case character
        if 64 < ascii_num < 91:
            ascii_num += shift
            if ascii_num > 90:
                ascii_num -= 26
            encrypted_text += chr(ascii_num)

    return encrypted_text























    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Create the encrypted string
    encrypted_text = ''
    for char in phrase:
        if char.isalpha():
            # Determine the position of the letter in the alclear
            phabet
            char_position = alphabet.index(char.lower())
            # Apply the shift and wrap around if necessary
            shifted_position = (char_position + shift) % 26
            # Convert the shifted position back to a letter
            encrypted_char = alphabet[shifted_position]
            # Preserve the case of the original letter
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            # Add the encrypted letter to the encrypted string
            encrypted += encrypted_char
        else:
            # Non-alphabetic characters are not encrypted
            encrypted += char
    return encrypted


# Create an encrypt function that takes in a plain text phrase and a numeric shift.
def encrypt_function(plain_text, shift):
#Plain text phrase  - i.e 26 letters
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#This line defines a string alphabet containing all lowercase letters of the English alphabet.
    encrypted_text = ''
  for letter in plain_text.lower():
        if letter.isalpha():
            shifted_index = (alphabet.index(letter) + shift) % 26
            encrypted_text += alphabet[shifted_index]
        else:
            encrypted_text += letter
    return encrypted_text










# if __name__ == '__main__':
#     pass