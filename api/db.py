from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQL_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Package(Base):
    __tablename__ = "package"

    id = Column(Integer, primary_key=True, index=True)


class Elf(Base):
    __tablename__ = "elf"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
