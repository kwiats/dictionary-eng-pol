from string import ascii_letters
from random import choice

def gen_list(quantity: int ):
    lst = []
    for _ in range(quantity):
        randList = {
            "word": choice(ascii_letters),
            "translated_word": choice(ascii_letters),
        }
        lst.append(randList)
    return lst
