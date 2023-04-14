import string
from corpus import word_list, namelist








def encrypt_function(phrase: str, shift: int) -> str:
    """
    Encrypts the given plain text phrase by shifting each letter in the phrase
    by the specified numeric shift. Shifts that exceed 26 wrap around, and shifts
    that push a letter out of range also wrap around.
    
    :param phrase: The plain text phrase to be encrypted.
    :param shift: The numeric shift used for encryption.
    :return: The encrypted string.
    """
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
#     # print(encrypt("cat", 3)) #e
#     # print(decrypt("olssv", 7)) # hello
#     # print(crack("olssv"))
#     pass