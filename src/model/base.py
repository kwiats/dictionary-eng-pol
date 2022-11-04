from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

word_category = Table(
    "word_category",
    Base.metadata,
    Column("word_id", Integer, ForeignKey("words.id")),
    Column("category_id", Integer, ForeignKey("category.id")),
)


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String)
    translated_word = Column(String)

    def __repr__(self) -> str:
        return f"<Words(id= {self.id}, word={self.word}, translated_word={self.translated_word}"


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)

    words = relationship("Word", secondary=word_category, backref="words")

    def __repr__(self) -> str:
        return f"<Category(id= {self.id}, category={self.category}"


engine = create_engine("postgresql://localhost/pawelkwiatkowski", echo=True)
Base.metadata.create_all(engine)
