from src.model.handling_base import get_all_category, get_all_words, get_category, get_words, get_words_from_category
from src.libs.utils import input_standard, split_to_pages, show_pages

if __name__ == "__main__":
    words = get_all_words()
    for row in words:
        print(row.id, row.word, row.translated_word)

    words = get_words("Hi")
    for row in words:
        print(row.id, row.word, row.translated_word)