"""
Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate the required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.
NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.
FOR EXAMPLE:
    characters = "cbacba"
    phrase = "aabbccc"
    In this case you CANNOT create required phrase, because you are 1 character short!
IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.
    You can always generate an empty string.
"""

characters = "cb acdba"
phrase = "aab c"


def generate_phrase(characters, phrase):
    set1 = list(characters)  # convert string to list
    set2 = list(phrase)
    counter = 0  # keep count of matching pairs

    try:
        for each in set2:  # go through each element in the phrase
            if each in set1:  # see if each element matches with characters
                set1.remove(each)  # if a match is found remove the matched item from characters
                counter += 1  # count how many matches were made
    except IndexError:
        return False

    finally:
        if len(set2) == counter:  # if number of matches equals the number of elements in the phrase
            return True
        else:
            return False


print(generate_phrase(characters, phrase))
