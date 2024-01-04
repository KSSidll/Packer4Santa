from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

import api.db
from api.db import get_db

router = APIRouter(
    prefix='/package',
    tags=['package'],
)


class PackageBase(BaseModel):
    description: str | None = None
    elf_id: int


class PackageAdd(PackageBase):
    pass


class PackageUpdate(PackageAdd):
    pass


class Package(PackageUpdate):
    id: int

    class Config:
        orm_mode = True


@router.get('/', response_model=list[Package])
def get_all_packages(db: Session = Depends(get_db)):
    return db.query(api.db.Package).all()


@router.get('/{package_id}', response_model=Package)
def get_package(package_id: int, db: Session = Depends(get_db)):
    package = db.query(api.db.Package).filter(api.db.Package.id == package_id).first()
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return package


@router.get('/elf/{elf_id}', response_model=list[Package])
def get_all_packages_by_elf_id(elf_id: int, db: Session = Depends(get_db)):
    return db.query(api.db.Package).filter(api.db.Package.elf_id == elf_id).all()


@router.post('/', response_model=Package)
def add_package(package: PackageAdd, db: Session = Depends(get_db)):
    db_elf = db.query(api.db.Elf).filter(api.db.Elf.id == package.elf_id).first()
    if db_elf is None:
        raise HTTPException(status_code=404, detail="Elf not found")

    db_package = api.db.Package(description=package.description, elf_id=package.elf_id)
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package


@router.put('/{package_id}', response_model=Package)
def update_package(package_id: int, package: PackageUpdate, db: Session = Depends(get_db)):
    db_elf = db.query(api.db.Elf).filter(api.db.Elf.id == package.elf_id).first()
    if db_elf is None:
        raise HTTPException(status_code=404, detail="Elf not found")

    db_package = db.query(api.db.Package).filter(api.db.Package.id == package_id).first()
    if db_package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    db.delete(db_package)

    db_package = api.db.Elf(id=package_id, description=package.description, elf_id=package.elf_id)
    db.add(db_package)
    db.commit()
    return db_package


@router.delete('/{package_id}', response_model=Package)
def delete_package(package_id: int, db: Session = Depends(get_db)):
    package = db.query(api.db.Package).filter(api.db.Package.id == package_id).first()
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    db.delete(package)
    db.commit()
    return package
