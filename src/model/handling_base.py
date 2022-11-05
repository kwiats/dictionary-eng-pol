from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from base import Word, Category, word_category, engine, Base

Session = sessionmaker(bind=engine)

session = Session()


def get_all_words(session: Session):
    return session.query(Word).all()


def get_all_category(session: Session):
    return session.query(Category).all()


def get_words_from_category(session: Session, category: str):
    return session.query(category.words).filter(category == category).all()


def get_words(session: Session, word: str = None, translated_word: str = None):
    if word:
        return session.query(Word).filter(word == word).all()
    return session.query(Word).filter(translated_word=translated_word).all()


def get_category(session: Session, category: str):
    return session.query(Category).filter(category == category).all()


def add_new_word(session: Session, input_word: str, input_trasnlated_word: str):
    word = (
        session.query(Word)
        .filter(Word.word == input_word)
        .filter(Word.translated_word == input_trasnlated_word)
        .one_or_none()
    )
    if word is not None:
        return

    word = Word(word=input_word, translated_word=input_trasnlated_word)

    return word


def add_new_category(session: Session, input_category: str):
    category = (
        session.query(Category)
        .filter(Category.category == input_category)
        .one_or_none()
    )
    if category is not None:
        return

    category = Category(category=input_category)

    return category


def add_new_word_category(word, category):
    return category.words.append(word)


# word = add_new_word(session=session, input_word="Hi", input_trasnlated_word="Siema")

# category = add_new_category(session=session, input_category="Greetings")

# print(word, category)

# add_new_word_category(word=word, category=category)

# session.add(category)
# session.commit()

words = get_all_words(session=session)

