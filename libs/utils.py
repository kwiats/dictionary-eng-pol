from typing import List

from gen_list import gen_list


def input_standard(input: str) -> str:
    """Input standardization which convert all upper letter to lower, replace numbers and other to empty

    Args:
        input (str): input which will be converted to standard input

    Returns:
        str: converted inputy
    """
    input = input.lower().strip()
    for letter in input:
        if not letter.isalpha():
            input = input.replace(letter, "")
    return input


def split_to_pages(lst: List) -> List:
    """Spliting dictionary to pages. One pages is for 10 elements.

    Args:
        lst (Dict): Dictionary which is converted to list

    Returns:
        List: Splited dictionary and converted to list.
    """

    pages = []
    i = 0
    lenght_lst = len(lst)

    if lenght_lst < 10:
        return lst

    quantityPages = lenght_lst // 10
    if (lenght_lst / 10) > (lenght_lst // 10):
        quantityPages += 1

    for _ in range(0, quantityPages):
        pages.append(lst[i : i + 10])
        i += 10

    return pages


def show_pages(in_pages: List):
    """Showing in console quantity of pages and elements for single page

    Args:
        in_pages (List): Splited list with elements
    """
    # tutaj dodac mozliwosc enterowania iteracji przez list 'in_pages'
    lenght_pages = len(in_pages)
    for page, _ in enumerate(in_pages):
        j = page + 1
        print(f"{j}/{lenght_pages}")
        for val in iterate_list(in_pages, page):
            print(val)

    # dodac mozliwosc przewiajania stron za pomoca komendy 'next'
    # oraz wyswietlanie pojedynczego elementu wykonuje sie po kliknieciu ENTER


def iterate_list(lst: List, indexPage: int):
    """Iterate elements in list

    Args:
        lst (List): List
        indexPage (int): Index of page

    Yields:
        string: output iterated element
    """
    for i, values in enumerate(lst[indexPage]):
        yield f"{i+1} > \t {values['word']} -> {values['translated_word']}"

