### wyswietlanie kilku wyrazow oraz sprawdzanie ich poprawnosci za kazdy poprawny wyraz +1 punkty
### 30 sekund w trakcie trwania musisz wpisac jak najwiecej slow
### znaki polskie, duze litery, male litery sa pomijane!!
### znaki specjalne sa bledami
from typing import List
from utils import input_standard
### wyswietlac: bledne slowa,


def check_correction(translated_word: str, input: str) -> bool:
    if input == translated_word:
        return True
    return False

def random_elemnts(quantity: int, lst: List):
    for 


print(check_correction("siema",input_standard("S1iema")))