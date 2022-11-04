from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Word, Category, word_category, engine, Base

Session = sessionmaker(bind = engine)

session = Session()

def add_new_word(session: Session, input_word: str, input_trasnlated_word: str):

    word = (session.query(Word).filter(Word.word == input_word).filter(Word.translated_word == input_trasnlated_word).one_or_none())
    if word is not None:
        return
    
    word = Word(word = input_word, translated_word = input_trasnlated_word)

    session.add(word)

    session.commit()


def add_new_category(session: Session, input_category: str):
    category = (session.query(Category).filter(Category.category == input_category).one_or_none())
    if category is not None:
        return 
    
    category = Category(category = input_category)
    
    session.add(category)

    session.commit()

def get_word_id(session: Session, input_word: str, input_translated_word: str):
    word_id = session.query(Word.id).filter(Word.word == input_word).filter(Word.translated_word == input_translated_word).first()
    return word_id[0]

def get_category_id(session: Session, input_category: str):
    category_id = session.query(Category.id).filter(Category.category == input_category).first()
    return category_id[0]

def add_word_category(session: Session, word_id: int, category_id: int):
    word_cat = (session.query(word_category).filter(word_category.word_id == word_id).filter(word_category.category_id == category_id).one_or_none())
    if word_cat is not None:
        return 
    
    word_cat = word_category(word_id = word_id, category_id=category_id)

    session.add(word_cat)

    session.commit()

add_new_word(session=session, input_word="Hi", input_trasnlated_word="Siema")

add_new_category(session=session, input_category="Greetings")

word_id = get_word_id(session=session, input_word="Hi", input_translated_word="Siema")
cat_id = get_category_id(session=session, input_category="Greetings")

add_word_category(session=session, word_id=word_id, category_id=cat_id)