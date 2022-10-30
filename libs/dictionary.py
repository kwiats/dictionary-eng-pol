import sqlite3

from os import path, chdir, getcwd
import pathlib

from configurations import DBNAME, PATH_TO_DB


def check_status(func):
    def wrapper(*args, **kwargs):
        if path.isfile(path.abspath(getcwd()) + PATH_TO_DB + DBNAME):
            return func(*args, **kwargs)
        raise FileExistsError("DataBase doesn't exists or cannot be created.")

    return wrapper


class Dictionary:
    def __init__(self, filename: str):
        self.connect = sqlite3.connect(path.abspath(getcwd()) + PATH_TO_DB + DBNAME)
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

    def close_and_commit(self):
        self.connect.commit()
        self.connect.close()

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


eng2pol = Dictionary(FILENAME)
