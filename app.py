from src.model.handling_base import get_all_category, get_all_words, get_category, get_words, get_words_from_category
from src.libs.utils import input_standard, split_to_pages, show_pages

if __name__ == "__main__":
# wprowadzanie danych 
    word = input("Word:")
    trs = input("Translation:")

    print(f"{word} -> {trs}")

    cat = input("Category:")

    print(f"{cat}: {word} -> {trs}")