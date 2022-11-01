### wyswietlanie kilku wyrazow oraz sprawdzanie ich poprawnosci za kazdy poprawny wyraz +1 punkty
### 30 sekund w trakcie trwania musisz wpisac jak najwiecej slow
### znaki polskie, duze litery, male litery sa pomijane!!
### znaki specjalne sa bledami
from typing import List
from utils import input_standard
from random import randint
### wyswietlac: bledne slowa,

from gen_list import gen_list

def check_correction(translated_word: str, input: str) -> bool:
    if input == translated_word:
        return True
    return False

def random_elemnts(quantity: int, lst: List):
    elements = ([randint(1, len(lst)) for _ in range(quantity)])
    return elements
    

lst = gen_list(30)
print(random_elemnts(10, lst))
print(check_correction("siema",input_standard("S1iema")))