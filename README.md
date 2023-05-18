# 401 Python Class 18

## LAB - Class 18

## Project: caeser-cipher

## Author: Dominick Martin 

### Feature Tasks and Requirements:

Create an encrypt function that takes in a plain text phrase and a numeric shift.the phrase will then be shifted that many letters.

E.g. encrypt(‘abc’,1) would return ‘bcd’. = E.g. encrypt(‘abc’, 10) would return ‘klm’.

shifts that exceed 26 should wrap around.E.g. encrypt(‘abc’,27) would return ‘bcd’.

shifts that push a letter out or range should wrap around.E.g. encrypt(‘zzz’,1) would return ‘aaa’.

Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.

create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.

Devise a method for the computer to determine if code was broken with minimal human guidance.


## Links and Resources Utilized:

ChatGPT 
Fellow Students Examples
TA Assistance 

## Setup

.venv
pip install pytest
Pip3 Install requirements.txt

pip install -r requirements.txt

run app with:
python3 caesar_cipher/cipher.py

run pytest with:
pytest tests/test_caesar.py 


## Link to Code

[Code](/cipher.py)


## How to initialize/run your application (where applicable)

to run program:

N/A

## How to use your library (where applicable)

N/A

## Tests

pytest