#create an empty string, name it "encrypted_word"
#loop through the word and check if each character is a small letter, capital or not
#if its a small letter, get the uniCode, subtract the unicode of 'a' to remove the unicode values and make it start from 1-26, add 13 then find the remainder of the result
# so as to prevent it from overlapping the 26 alphabet then add the unicode of "a" then get back the char character
#do the same for capital letter while getting the string character keep adding it to the empty string.
#add the rest directly inside the empty string. Return the String
#97-123


def encrypt(word):
    encrypted_word = ""

    for character in word:
        if 'a' <= character <= 'z':
            encrypted_word += chr(((ord(character) - ord('a') + 13 ) % 26 ) + ord('a'))
        elif 'A' <= character <= 'Z':
            encrypted_word += chr(((ord(character) - ord('A') + 13 ) % 26 ) + ord('A'))
        else:
            encrypted_word += character
        #encrypted_word += chr(ord(character) + 13)
    return encrypted_word



