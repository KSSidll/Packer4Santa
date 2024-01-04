from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

import api
from api.db import get_db, HolidayStatus

router = APIRouter(
    prefix='/elf',
    tags=['elf'],
)


class ElfBase(BaseModel):
    name: str | None = None


class ElfAdd(ElfBase):
    pass


class ElfUpdate(ElfAdd):
    holiday_status: HolidayStatus = HolidayStatus.NONE


class Elf(ElfUpdate):
    id: int

    class Config:
        orm_mode = True


@router.get('/', response_model=list[Elf])
def get_all_elves(db: Session = Depends(get_db)):
    return db.query(api.db.Elf).all()


@router.get('/{elf_id}', response_model=Elf)
def get_elf(elf_id: int, db: Session = Depends(get_db)):
    elf = db.query(api.db.Elf).filter(api.db.Elf.id == elf_id).first()
    if elf is None:
        raise HTTPException(status_code=404, detail="Elf not found")
    return elf


@router.post('/', response_model=Elf)
def add_elf(elf: ElfAdd, db: Session = Depends(get_db)):
    db_elf = api.db.Elf(name=elf.name)
    db.add(db_elf)
    db.commit()
    db.refresh(db_elf)
    return db_elf


@router.put('/{elf_id}', response_model=Elf)
def update_elf(elf_id: int, elf: ElfUpdate, db: Session = Depends(get_db)):
    db_elf = db.query(api.db.Elf).filter(api.db.Elf.id == elf_id).first()
    if db_elf is None:
        raise HTTPException(status_code=404, detail="Elf not found")
    db.delete(db_elf)

    db_elf = api.db.Elf(id=elf_id, name=elf.name, holiday_status=elf.holiday_status)
    db.add(db_elf)
    db.commit()
    return db_elf


@router.delete('/{elf_id}', response_model=Elf)
def delete_elf(elf_id: int, db: Session = Depends(get_db)):
    elf = db.query(api.db.Elf).filter(api.db.Elf.id == elf_id).first()
    if elf is None:
        raise HTTPException(status_code=404, detail="Elf not found")
    db.delete(elf)
    db.commit()
    return elf
