from msilib.schema import Error
import sqlite3
from os import path, getcwd

from configurations import DBNAME, PATH_TO_DB

ABSPATH = path.abspath(getcwd())


def check_status(func):
    def wrapper(*args, **kwargs):
        if path.isfile(ABSPATH + PATH_TO_DB + DBNAME):
            return func(*args, **kwargs)
        raise FileExistsError("DataBase doesn't exists or cannot be created.")

    return wrapper


class Dictionary:
    def create_data_base(self, filename: str = DBNAME):
        """Create database in SQLite3 with path and filename from configurations.py

        Args:
        filename(str): name of file database. Default retrive from configurations.py
        """

        self.connect = sqlite3.connect(ABSPATH + PATH_TO_DB + filename)
        self.cursor = self.connect.cursor()

    @check_status
    def create_main_table(self):
        """Create main table with all words, translated word and index"""

        create_table = """CREATE TABLE IF NOT EXISTS words(
            wordId INTEGER PRIMARY KEY,
            word TEXT,
            translatedWord TEXT)"""
        return self.cursor.execute(create_table)

    @check_status
    def create_category_table(self):
        """Create category table for database with index and name"""

        create_table = """CREATE TABLE IF NOT EXISTS category(
            categoryId INTEGER PRIMARY KEY,
            category TEXT)"""
        return self.cursor.execute(create_table)

    @check_status
    def create_wordcategory_table(self):
        """Create word category table for database with index of word and index of category"""
        create_table = """CREATE TABLE IF NOT EXISTS wordCategory(
            wordId INTEGER NOT NULL, 
            categoryId INTEGER NOT NULL,
            FOREIGN KEY(wordId) REFERENCES words(wordId),
            FOREIGN KEY(categoryId) REFERENCES category(categoryId))"""
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
    def insert_word(self, word: str, translated: str):
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

    @check_status
    def insert_category(self, category: str):
        self.cursor.execute(
            f"""
            INSERT INTO category(category)
            VALUES ('{category}')
            """
        )

        return self.cursor.fetchall()

    @check_status
    def update_category(
        self, id: int = None, category: str = None, new_category: str = None
    ):
        if id:
            query = f"""UPDATE category SET category = '{category}' WHERE categoryId = '{id}'"""
            updated = self.cursor.execute(query)
            return updated.fetchone()
        if category and category:
            query = f"""UPDATE category SET category = '{category}' WHERE category = '{new_category}'"""
            updated = self.cursor.execute(query)
            return updated.fetchone()
        return None

    @check_status
    def delete_category(self, id: int = None, category: str = None):
        if id:
            query = f"""DELETE FROM category WHERE categoryId = '{id}'"""
            deleted = self.cursor.execute(query)
            return deleted.fetchone()
        if category:
            query = f"""DELETE FROM category WHERE category = '{category}'"""
            deleted = self.cursor.execute(query)
            return deleted.fetchone()
        return None

    @check_status
    def find_id_word(self, word: str):
        query = f"""SELECT wordId FROM words WHERE word = '{word}' """
        wordId = self.cursor.execute(query)
        return wordId.fetchone()

    @check_status
    def find_id_cat(self, category: str):
        query = f"""SELECT categoryId FROM category WHERE category = '{category}' """
        categoryId = self.cursor.execute(query)
        return categoryId.fetchone()

    @check_status
    def insert_word_category(self, wordId: int, categoryId: int):
        query = f"""
            INSERT INTO wordCategory(wordId, categorId)
            VALUES ('{wordId}', '{categoryId}')
            """
        self.cursor.execute(query)
        self.cursor.commit()

    @check_status
    def update_word_category(self, wordId: int, categoryId: int, option: int = 1):
        if option == 1:
            query = f"""UPDATE wordCategory SET cateogryId = '{categoryId}' WHERE wordId = '{wordId}'"""
            updated = self.cursor.execute(query)
            return updated.fetchone()
        elif option == 2:
            query = f"""UPDATE wordCategory SET wordId = '{wordId}' WHERE cateogryId = '{categoryId}'"""
            updated = self.cursor.execute(query)
            return updated.fetchone()
        else:
            raise Error("Only two option,1# change categoryId or 2# change wordId")

    @check_status
    def delete_category(self, wordId: int = None, categoryId: int = None):
        if wordId:
            query = f"""DELETE FROM wordCategory WHERE wordId = '{wordId}'"""
            deleted = self.cursor.execute(query)
            return deleted.fetchone()
        if categoryId:
            query = f"""DELETE FROM wordCategory WHERE categoryId = '{categoryId}'"""
            deleted = self.cursor.execute(query)
            return deleted.fetchone()


eng2pol = Dictionary()
eng2pol.create_data_base()
eng2pol.create_main_table()
eng2pol.create_category_table()
eng2pol.create_wordcategory_table()
# eng2pol.insert_element("test", "test1")
# words = eng2pol.show_all()
# print(words)
# eng2pol.update_element("test2", wordIndex=1)
# words = eng2pol.show_all()
# print(words)
# eng2pol.update_element("test3", word="test")
# words = eng2pol.show_all()
# print(words)
