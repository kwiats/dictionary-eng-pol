from sqlalchemy.orm import sessionmaker

from base import Word, Category, engine

Session = sessionmaker(bind=engine)

session = Session()


def get_all_words():
    return session.query(Word).all()


def get_all_category():
    return session.query(Category).all()


def get_words_from_category(category):
    return category.words


def get_words(word: str = None, translated_word: str = None):
    if word:
        return session.query(Word).filter_by(word = word).all()
    return session.query(Word).filter_by(translated_word = translated_word).all()


def get_category(category: str):
    return session.query(Category).filter_by(category = category).first()


def add_new_word(input_word: str, input_translated_word: str):
    word = (
        session.query(Word)
        .filter(Word.word == input_word)
        .filter(Word.translated_word == input_translated_word)
        .one_or_none()
    )
    if word is not None:
        return

    word = Word(word=input_word, translated_word=input_translated_word)

    return word


def add_new_category(input_category: str):
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

# TEST
# food = add_new_category(input_category="FOOD")
# strawberry = add_new_word(input_word="Strawberry", input_translated_word="Truskawka")
# apple = add_new_word(input_word="Apple", input_translated_word="Jabłko")

# adj = add_new_category(input_category="ADJECTIVES")
# nice = add_new_word(input_word="Nice", input_translated_word="Miły")
# lovable = add_new_word(input_word="Lovable", input_translated_word="Sympatyczny")

# add_new_word_category(strawberry, food)
# add_new_word_category(apple, food)

# add_new_word_category(nice, adj)
# add_new_word_category(lovable, adj)

# session.add_all([adj, food])               
# session.commit()

food = get_category("FOOD")
print(food)

adj = get_category("ADJECTIVES")
print(adj)

food_words = get_words_from_category(food)
print(food_words)

for x in food_words:
    print(f"{x.id} {x.word} -> {x.translated_word}")

adj_words = get_words_from_category(adj)
print(adj_words)

for x in adj_words:
    print(f"{x.id} {x.word} -> {x.translated_word}")


words = get_all_words()

for x in words:
    print(x)

categories = get_all_category()

for x in categories:
    print(x)

word_1 = get_words(word="Nice")
print(word_1)
word_2 = get_words(translated_word="Truskawka")
print(word_2)
