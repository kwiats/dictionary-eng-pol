from string import ascii_letters
from random import choice

ranList = {}

def gen_list():
    for _ in range(30):
        letter_1 = choice(ascii_letters)
        letter_2 = choice(ascii_letters)
        ranList[letter_1] = letter_2
    return ranList


print(gen_list())