from enum import Enum

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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


class HolidayStatus(Enum):
    NONE = 0
    PATERNITY_LEAVE = 1
    VACATION = 2
    SICK_LEAVE = 3
    OTHER = 4


class Package(Base):
    __tablename__ = "package"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    elf_id = Column(Integer, ForeignKey("elf.id"))

    elf = relationship("Elf", back_populates="packages")


class Elf(Base):
    __tablename__ = "elf"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    holiday_status = Column(sqlalchemy.Enum(HolidayStatus), default=HolidayStatus.NONE)

    packages = relationship("Package", back_populates="elf")
