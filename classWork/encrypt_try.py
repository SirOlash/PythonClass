import string
from operator import indexOf


def encrypt(word):
    encrypted_word = ""

    for letter in word:
        if letter.islower():
            for character in string.ascii_lowercase:
                if letter == character:
                    character_index = (indexOf(string.ascii_lowercase, letter) + 13) % 26
                    encrypted_word += string.ascii_lowercase[character_index]
        elif letter.isupper():
            for character in string.ascii_uppercase:
                if letter == character:
                    character_index = (indexOf(string.ascii_lowercase, letter) + 13) % 26
                    encrypted_word += string.ascii_lowercase[character_index]
        else:
            encrypted_word += letter
    return encrypted_word

