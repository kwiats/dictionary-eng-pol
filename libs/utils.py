from curses.ascii import isdigit
from typing import List


def input_standard(input: str) -> str:
    input = input.lower().strip()
    for letter in input:
        if not letter.isalpha():
            input = input.replace(letter, "")
    return input


def to_pages(lst: List) -> List:
    pages = []
    i = 0
    lenght_lst = len(lst)

    if lenght_lst < 10:
        return lst

    amountPages = lenght_lst % 10
    for amount in range(0, amountPages):
        pages.append(lst[i : i + 10])
        i += 10

    return pages


def show_pages(in_pages: List):
    # tutaj dodac mozliwosc enterowania iteracji przez list 'in_pages'
    lenght_pages = len(in_pages)
    for i, _ in enumerate(in_pages):
        print(f"{i+1}/{lenght_pages}")

    # dodac mozliwosc przewiajania stron za pomoca komendy 'next'
    # oraz wyswietlanie pojedynczego elementu wykonuje sie po kliknieciu ENTER
