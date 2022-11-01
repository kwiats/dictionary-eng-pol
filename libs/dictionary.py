from operator import index
import sqlite3

from os import path, getcwd

from configurations import DBNAME, PATH_TO_DB, DEFAULT_NAME

ABSPATH = path.abspath(getcwd())


def check_status(func):
    def wrapper(*args, **kwargs):
        if path.isfile(ABSPATH + PATH_TO_DB + DBNAME):
            return func(*args, **kwargs)
        raise FileExistsError("DataBase doesn't exists or cannot be created.")

    return wrapper


class Dictionary:
    def create_data_base(self, filename: str):
        self.connect = sqlite3.connect(ABSPATH + PATH_TO_DB + filename)
        self.cursor = self.connect.cursor()

    @check_status
    def create_main_table(self, name: str = DEFAULT_NAME):
        """Create main table with all words, translated word and specific category"""

        create_table = """CREATE TABLE IF NOT EXISTS '{name}'(
            wordId INTEGER PRIMARY KEY,
            word TEXT,
            translatedWord TEXT,
            categoryId INTEGER)"""
        return self.cursor.execute(create_table)

    @check_status
    def create_category_table(self):
        """Create category table for database with index and name"""

        create_table = """CREATE TABLE IF NOT EXISTS category(
            categoryId INTEGER PRIMARY KEY,
            name TEXT)"""
        return self.cursor.execute(create_table)

    # def close_and_commit(self):
    #     self.connect.commit()
    #     self.connect.close()

    @check_status
    def show_terms(self, term: str):
        """Retrive all elements with specific term or without it

        Args:
            term (str, optional): specific term to show up. Defaults to None.

        Returns:
            List: elements from database
        """
        if term:
            self.cursor.execute(f"SELECT * FROM words WHERE word = '{term}'")

            return self.cursor.fetchall()
        return None

    @check_status
    def show_all(self):
        """Retrive all elements from database

        Returns:
            List: all elements from database
        """
        self.cursor.execute(f"SELECT * FROM words")

        return self.cursor.fetchall()

    @check_status
    def insert_element(self, word: str, translated: str):
        """Insert element with specific word and translated word to database.

        Args:
            word (str): word in other language
            translated (str): translated word in your needed language

        Returns:
            List: elements from database
        """
        self.cursor.execute(
            f"""
            INSERT INTO words(word, translated_word)
            VALUES ('{word}', '{translated}')
            """
        )

        return self.cursor.fetchall()

    @check_status
    def update_translation(
        self, translated: str, word: str = None, wordIndex: int = None
    ):
        """sumary_line

        Args:
            argument(type): description

        Returns:
            return(type): description
        """

        if wordIndex:
            query = f"""UPDATE words SET translated_word = '{translated}' WHERE wordId = '{wordIndex}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        if word:
            query = f"""UPDATE words SET translated_word = '{translated}' WHERE word = '{word}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        return None

    @check_status
    def delete_word(self, word: str = None, wordIndex: int = None):
        if wordIndex:
            query = f"""DELETE FROM words WHERE wordId = '{wordIndex}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        if word:
            query = f"""DELETE FROM words WHERE word = '{word}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        return None

    def insert_category():
        pass

    def update_category():
        pass

    def delete_category():
        pass


eng2pol = Dictionary()
eng2pol.create_data_base(DBNAME)
eng2pol.create_main_table()
eng2pol.create_category_table()
# eng2pol.insert_element("test", "test1")
# words = eng2pol.show_all()
# print(words)
# eng2pol.update_element("test2", wordIndex=1)
# words = eng2pol.show_all()
# print(words)
# eng2pol.update_element("test3", word="test")
# words = eng2pol.show_all()
# print(words)
