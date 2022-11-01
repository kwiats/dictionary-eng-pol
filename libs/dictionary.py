from operator import index
import sqlite3

from os import path, chdir, getcwd
import pathlib

from configurations import DBNAME, PATH_TO_DB

ABSPATH = path.abspath(getcwd())


def check_status(func):
    def wrapper(*args, **kwargs):
        if path.isfile(ABSPATH + PATH_TO_DB + DBNAME):
            return func(*args, **kwargs)
        raise FileExistsError("DataBase doesn't exists or cannot be created.")

    return wrapper


class Dictionary:
    def __init__(self, filename: str):
        self.connect = sqlite3.connect(ABSPATH + PATH_TO_DB + filename)
        self.cursor = self.connect.cursor()

    @check_status
    def define_data_base(self):
        """Create SQL file with table - term and translated

        Args:
            filename (str, optional): Name of sql file. Defaults to "english-polish.db".


        """

        create_table = """CREATE TABLE IF NOT EXISTS words(
            wordId INTEGER PRIMARY KEY,
            word TEXT,
            translated_word TEXT)"""
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
    def update_element(self, translated: str, word: str = None, index_element: int = None):
        """sumary_line
        
        Args:
            argument(type): description

        Returns: 
            return(type): description
        """
        
    
        if index_element:
            query = f"""UPDATE words SET translated_word = '{translated}' WHERE wordId = '{index_element}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        if word:
            query = f"""UPDATE words SET translated_word = '{translated}' WHERE word = '{word}'"""
            self.cursor.execute(query)
            return self.cursor.fetchone()
        return None

    @check_status
    def delete_element(self, word: str = None, index_element: int = None):
        pass


eng2pol = Dictionary(DBNAME)
eng2pol.define_data_base()
eng2pol.insert_element("test", "test1")
words = eng2pol.show_all()
print(words)
eng2pol.update_element("test2", index_element=1)
words = eng2pol.show_all()
print(words)
eng2pol.update_element("test3", word="test")
words = eng2pol.show_all()
print(words)
