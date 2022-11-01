from curses.ascii import isdigit
from typing import Dict, List


def input_standard(input: str) -> str:
    input = input.lower().strip()
    for letter in input:
        if not letter.isalpha():
            input = input.replace(letter, "")
    return input


def to_pages(lst: Dict) -> List:
    lst = list(lst.items())
    pages = []
    i = 0
    lenght_lst = len(lst)

    if lenght_lst < 10:
        return lst

    quantityPages = 0
    if (lenght_lst / 10) > (lenght_lst // 10):
        quantityPages = (lenght_lst // 10) + 1

    for _ in range(0, quantityPages):
        pages.append(lst[i : i + 10])
        i += 10

    return pages


def show_pages(in_pages: List):
    # tutaj dodac mozliwosc enterowania iteracji przez list 'in_pages'
    lenght_pages = len(in_pages)
    for i, _ in enumerate(in_pages):
        j = i+1
        print(f"{j}/{lenght_pages}")
        for l, v in enumerate(in_pages[i]):
            print(f"{l+1} > {v}")

    # dodac mozliwosc przewiajania stron za pomoca komendy 'next'
    # oraz wyswietlanie pojedynczego elementu wykonuje sie po kliknieciu ENTER

lst = {'U': 'F', 'n': 'W', 'l': 'g', 'J': 'Z', 'H': 'o', 'e': 'Q', 'Q': 'm', 'd': 'm', 'v': 'c', 'm': 'h', 'K': 'e', 'i': 'F', 'y': 'G', 'L': 'i', 'r': 'f', 'N': 'x', 'f': 'F', 'b': 'y', 'k': 'W', 's': 'Y', 'V': 'M', 'X': 'g', 'F': 'u', 'j': 'O', 'a': 'S'}

pages = to_pages(lst)
show_pages(pages)