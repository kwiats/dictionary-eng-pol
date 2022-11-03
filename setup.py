from src.model.base import Base

from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("postgresql://localhost/pawelkwiatkowski", echo=True)
    Base.metadata.create_all(engine)