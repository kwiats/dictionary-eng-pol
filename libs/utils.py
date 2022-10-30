from curses.ascii import isdigit
from typing import List


def check_correction(translated_word: str, input: str) -> bool:
    if input == translated_word:
        return True
    return False

def input_standard(input: str ) -> str:
    input = input.lower().strip()
    for letter in input:
        if not letter.isalpha():
                input = input.replace(letter, "")
    return input

def show_in_pages(lst: List):
    pages = []
    i = 0
    lenght_lst = len(lst)
    if lenght_lst > 10:
        amountPages = lenght_lst % 10
        for amount in range(0, amountPages):
            pages.append(lst[i:i+10])
            i+=10
    

    #dodac mozliwosc przewiajania stron za pomoca komendy 'next' 
    # oraz wyswietlanie pojedynczego elementu wykonuje sie po kliknieciu ENTER

