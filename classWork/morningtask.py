# import string

def character_count(character):
    count = {}
    for char in character:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

    # print(list(character))
    # list(character)

def swap_character(string1, string2):
    new_string1 = string1[:2] + string1[2:]
    new_string2 = string2[:2] + string2[2:]
    return new_string1 + " " + new_string2


def divide_word(string):
    if len(string) % 2 == 0:
        new_string = string[:len(string)//2] + "ce" + string[len(string)//2:]
    else: new_string = string + "ce"
    return new_string

def upper_first(string):
    upper_string = ""
    lower_string = ""
    for char in string:
        if char.isupper():
            upper_string += char
        else:
            lower_string += char
    return upper_string + lower_string

def character_occurrences(string, character):
    occurrences = 0
    for char in string:
        if char == character:
            occurrences += 1
    return character , occurrences

def remove_special_character(string):
    new_string = ""
    for char in string:
        if char.isalpha() or char.isdigit():
            new_string += char
    return new_string

def dictionary_trial(string):
    dictionary = {}
    for char in string:
        dictionary[char] = 1
        return dictionary

    # return string1 + string2
    # grid = []
    #
    # for _ in range(3):
    #     row = []
    #     for _ in range(3):
    #         row.append("Cell.Empty")
    #     grid.append(row)
    # return grid

def esther_task(numbers):
    new_array = []
    for index in range(3):
        temp_array = []
        for index2 in range(1,-1,-1):
            temp_array.append(numbers[index2][index])
        new_array.append(temp_array)
    return new_array

print(esther_task([[12,13,14],[15,16,17]]))




# print(dictionary_trial())
# print(dictionary_trial("hello","joyce"))