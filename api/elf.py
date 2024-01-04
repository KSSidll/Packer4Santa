from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db import get_db

router = APIRouter(
    prefix='/elf',
    tags=['elf'],
)


class ElfBase(BaseModel):
    pass


class Elf(ElfBase):
    id: int

    class Config:
        orm_mode = True


@router.get('/all', response_model=list[Elf])
async def get_all_elves(db: Session = Depends(get_db)):
    return db.query(Elf).all()
