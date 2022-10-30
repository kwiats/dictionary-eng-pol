from typing import List

from dictionary import Dictionary
from configurations import DBNAME


class Default(Dictionary):
    def __init__(self, filename: str):
        super().__init__(filename)
        self.name = "Default"

    def __str__(self) -> str:
        return "You are used default list of words"


class OwnList(Dictionary):
    def __init__(self, nameList: str, filename: str):
        super().__init__(filename)
        self.nameList = nameList
        self.limitWords = 50

    def add_words(self, words: List):
        for word, trasnalted in words:
            pass

    def __str__(self) -> str:
        return f"You are used your own list of words {self.nameList}"


default_list = Default(DBNAME)
print(default_list)
